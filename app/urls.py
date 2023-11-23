# urls.py
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', views.start, name='start'),  # Asociar la URL raíz a la vista de inicio
    #path('login/', login, name='login'),
    path('register/', views.register_view, name='register'),    
    path('home/', home, name='home'),
]
