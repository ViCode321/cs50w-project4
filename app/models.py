from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to say'),
    ]
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)    
    location = models.CharField(max_length=100, blank=True, null=False)
    biography = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    last_activity = models.DateTimeField(auto_now=True)    
    
    def set_offline(self):
        self.last_activity = timezone.now()
        self.save()
    def __str__(self):
        return f'{self.username} ({self.location or "N/A"})'    

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
