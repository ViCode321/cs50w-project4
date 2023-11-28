from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms import RegistrationForm, UserProfileForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Post


def start(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

# views.py
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.set_online()  # Marca al usuario como en línea al iniciar sesión
            user.save_session_key(request)  # Guarda la clave de sesión en la base de datos
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    if request.user.is_authenticated:
        request.user.set_offline()  # Marca al usuario como fuera de línea al cerrar sesión
        request.user.session_key = None  # Elimina la clave de sesión de la base de datos
        request.user.save(update_fields=['session_key'])
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)           
        if form.is_valid():
            user = form.save()
            login(request, user)            
            # Envía el correo electrónico de bienvenida
            send_welcome_email(user.email, user.username)
            # Redirige a la página de inicio de sesión u otra página después del registro.
            return redirect('foto')
        else:
            return render(request, 'register.html', {'form': form})         
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def send_welcome_email(email, username):
    subject = f'¡Hola {username}! Bienvenido a Christians Together!'
    message = 'Gracias por registrarte en Christians Together. Esperamos que disfrutes de nuestra plataforma.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

@login_required
def foto_view(request):
    user = request.user
    location = user.location or 'Ubicación no disponible'

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'password': '********',  # Puedes obtener esto de la manera que desees
        'location': location,
        'email': user.email,
    } 
    return render(request, 'foto.html', context)

@login_required
def user_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            print('Perfil actualizado correctamente.')
            return redirect('foto')
        else:
            print('Error al actualizar el perfil. Por favor, corrija los errores.')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'foto.html', context)

def view_posts(request):
    posts = Post.objects.all()
    return render(request, 'view_posts.html', {'posts': posts})

def people(request):
    return render(request, 'people.html')

@login_required
def online_users(request):
    online_users = CustomUser.objects.filter(is_online=True)
    usernames = [user.username for user in online_users]
    return JsonResponse({'online_users': usernames})



