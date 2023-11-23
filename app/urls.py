# urls.py de app
from django.urls import path
from .views import home, logout_view, login_view, foto
from . import views

urlpatterns = [
    path('', login_view, name='start'),  # Redirige al login en la ruta raíz
#    path('', views.start, name='start'),  # Asociar la URL raíz a la vista de inicio
    path('login/', login_view, name='login'),    
#    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),    
    path('logout/', logout_view, name='logout'),
    path('foto/', foto, name='foto'),
    path('home/', home, name='home'),
]
