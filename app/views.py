from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms import RegistrationForm, UserProfileForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Post
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta

#------------------- Registro, Acceso y Salida de Usuario -------------------

#Acceso
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return render(request, 'login.html')
    return render(request, 'login.html')

#Registro
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)           
        if form.is_valid():
            user = form.save()
            login(request, user)            
            send_welcome_email(user.email, user.username)
            return redirect('foto')
        else:
            return render(request, 'register.html', {'form': form})         
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

#Salida
@login_required(login_url='login')
def logout_view(request):
    if request.user.is_authenticated:
        request.user.last_activity = timezone.now() - timedelta(minutes=0.10)
        request.user.save()
    logout(request)
    return redirect('login')

#------------------- Vista de Usuarios -------------------

#Bienvenida
def start(request):
    return render(request, 'welcome.html')

#Incio
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

#Perfil
@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

#------------------- Actividad de Usuarios -------------------

#Vista usuario en linea
@login_required(login_url='login')
def online_users(request):
    return render(request, 'online_users.html')

#Usuarios en linea
@login_required(login_url='login')
def online_users_json(request):
    active_users = CustomUser.objects.filter(last_activity__gte=timezone.now()-timedelta(minutes=0.10)).exclude(username=request.user.username)[:5]
    inactive_users = CustomUser.objects.filter(last_activity__lt=timezone.now()-timedelta(minutes=0.10)).exclude(username=request.user.username)[:5]
    active_user_list = [{'username': user.username, 'is_active': True, 'profile_picture': str(user.profile_picture.url) if user.profile_picture else None, 'biography': user.biography} for user in active_users]
    inactive_user_list = [{'username': user.username, 'is_active': False} for user in inactive_users]
    print(active_user_list + inactive_user_list)
    return JsonResponse({'users': active_user_list + inactive_user_list})

#------------------- Configuración de perfiles usuarios -------------------

#Vista de perfiles de usuarios
@login_required(login_url='login')
def foto_view(request):
    user = request.user
    location = user.location or 'Ubicación no disponible'

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'password': '********',
        'location': location,
        'email': user.email,
    } 
    return render(request, 'foto.html', context)

#Acualizar usuario
@login_required(login_url='login')
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

#------------------- Post de usuarios -------------------

#Vista de los posts
@login_required(login_url='login')
def view_posts(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

#Crear post
@login_required(login_url='login')
def create_post(request):
    return render(request, 'create_post.html')


#------------------- Funciones extra -------------------

#Enviar correo
def send_welcome_email(email, username):
    subject = f'¡Hola {username}! Bienvenido a Christians Together!'
    message = 'Gracias por registrarte en Christians Together. Esperamos que disfrutes de nuestra plataforma.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)



