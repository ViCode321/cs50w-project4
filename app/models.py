from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model

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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    bible_quote = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.user.username} at {self.publication_date}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post} at {self.comment_date}'
