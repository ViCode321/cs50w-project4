from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms import RegistrationForm
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

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
<<<<<<< HEAD
        print('Form is valid: ', form.is_valid())
        print('Form errors: ', form.errors)        
=======
>>>>>>> master
        if form.is_valid():
            user = form.save()
            login(request, user)            
            # Envía el correo electrónico de bienvenida
            send_welcome_email(user.email)
            # Redirige a la página de inicio de sesión u otra página después del registro.
            return redirect('home')
        else:
            messages.error(request, 'Hubo un error en el registro. Corrige los errores a continuación.')
<<<<<<< HEAD
            return render(request, 'register.html', {'form': form})            
    else:
        form = RegistrationForm()
=======
            return render(request, 'register.html', {'form': form})         
    else:
        form = RegistrationForm()

>>>>>>> master
    return render(request, 'register.html', {'form': form})

def send_welcome_email(email):
    subject = '¡Bienvenido a Christians Together!'
    message = 'Gracias por registrarte en Christians Together. Esperamos que disfrutes de nuestra plataforma.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
