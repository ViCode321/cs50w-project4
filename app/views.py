from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings

def start(request):
    return render(request, 'login.html')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('start')  # Reemplaza 'dashboard' con el nombre de tu vista de panel principal
        else:
            # Manejar el caso en el que la autenticación falla
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # Envía el correo electrónico de bienvenida
            send_welcome_email(user.email)
            # Redirige a la página de inicio de sesión u otra página después del registro.
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def send_welcome_email(email):
    subject = '¡Bienvenido a Christians Together!'
    message = 'Gracias por registrarte en Christians Together. Esperamos que disfrutes de nuestra plataforma.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
