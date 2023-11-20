from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.decorators import login_required


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
        # Obtener datos del formulario
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Crear nuevo usuario
        user = User.objects.create_user(username=username, email=email, password=password)

        # Crear instancia de Usuario personalizado
        usuario_personalizado = Users(user=user, Nombre=username, CorreoElectronico=email, Contraseña=password)
        usuario_personalizado.save()

        # Autenticar al nuevo usuario
        login(request, user)
        return redirect('start')  # Reemplaza 'dashboard' con el nombre de tu vista de panel principal
    else:
        return render(request, 'register.html')
