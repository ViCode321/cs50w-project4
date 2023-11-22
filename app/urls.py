# cristhians/urls.py
from django.urls import path
from .views import home, register_view
from . import views

urlpatterns = [
    path('', views.start, name='start'),  # Asociar la URL raíz a la vista de inicio
    #path('login/', login, name='login'),
    path('register/', register_view, name='register'),    
    path('home/', home, name='home'),
]
