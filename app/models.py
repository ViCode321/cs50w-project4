from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
from django.contrib.auth import get_user_model

class Users(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)  
    Username = models.CharField(max_length=255, unique=True)       
    Email = models.EmailField(unique=True)
    Gener = models.CharField(max_length=255)
    PerfilPhoto = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    Ubication = models.CharField(max_length=100, null=True, blank=True)
    Biography = models.TextField(null=True, blank=True)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )


class Group(models.Model):
    GroupID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.TextField(null=True, blank=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

class UserGroup(models.Model):
    User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Publication(models.Model):
    PublicationID = models.AutoField(primary_key=True)
    User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Content = models.TextField()
    PublicationDate = models.DateTimeField(auto_now_add=True)

class Coment(models.Model):
    ComentID = models.AutoField(primary_key=True)
    Publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Content = models.TextField()
    ComentDate = models.DateTimeField(auto_now_add=True)

class PrivateMessage(models.Model):
    MessageID = models.AutoField(primary_key=True)
    Transmitter = models.ForeignKey(get_user_model(), related_name='send_message', on_delete=models.CASCADE)
    Receptor = models.ForeignKey(get_user_model(), related_name='received_message', on_delete=models.CASCADE)
    Content = models.TextField()
    SendDate = models.DateTimeField(auto_now_add=True)
    Check = models.BooleanField(default=False)
=======


class CustomUser(AbstractUser):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to say'),
    ]

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=gender_choices)

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

class UserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

class PrivateMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
>>>>>>> master
