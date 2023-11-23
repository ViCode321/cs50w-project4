from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from app.models import CustomUser
from django.contrib.auth.decorators import login_required


def start(request):
    return render(request, 'login.html')

# Create your views here.
def home(request):
    return render(request, 'home.html')

from django.contrib.auth import get_user_model

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


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)           
        if form.is_valid():
            user = form.save()
            login(request, user)            
            # Envía el correo electrónico de bienvenida
            send_welcome_email(user.email)
            # Redirige a la página de inicio de sesión u otra página después del registro.
            return redirect('foto')
        else:
            return render(request, 'register.html', {'form': form})         
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def send_welcome_email(email):
    subject = '¡Bienvenido a Christians Together!'
    message = 'Gracias por registrarte en Christians Together. Esperamos que disfrutes de nuestra plataforma.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def foto_view(request):
    user = request.user
    location = request.POST.get('location_hidden')  # Obtener el valor del campo oculto

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'password': '********',  # Puedes obtener esto de la manera que desees
        'location': location,  # Usar el valor del campo oculto
        'email': user.email,
    }

    return render(request, 'foto.html', context)







