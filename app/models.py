from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to say'),
    ]

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)    
    location = models.CharField(max_length=100, blank=False, null=False)
    biography = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    is_online = models.BooleanField(default=False)
    session_key = models.CharField(max_length=32, blank=True, null=True)

    def set_online(self):
        self.is_online = True
        self.save(update_fields=['is_online'])

    def set_offline(self):
        self.is_online = False
        self.save(update_fields=['is_online'])

    def save_session_key(self, request):
        self.session_key = request.session.session_key
        self.save(update_fields=['session_key'])
    def check_password(self, raw_password):
        return super().check_password(raw_password)
    
    def __str__(self):
        return f'{self.username} ({self.location or "N/A"})'    

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
