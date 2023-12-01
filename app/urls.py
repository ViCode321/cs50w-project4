# urls.py de app
from django.urls import path
from .views import logout_view, login_view, foto_view
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.start, name='start'),  # Redirige al login en la ruta raíz
    path('login/', login_view, name='login'),    
    path('register/', views.register_view, name='register'),    
    path('logout/', logout_view, name='logout'),
    path('foto/', foto_view, name='foto'),
    path('home/', views.view_posts, name='home'),
    path('user_profile/', views.user_profile, name='user_profile'),    
    path('profile/', views.profile, name='profile'),
    path('online_users/', views.online_users, name='online_users'),
    path('online_users_json/', views.online_users_json, name='online_users_json'),
    path('post/', views.view_posts2, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),

]

# Configuración para servir archivos estáticos y de medios en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)