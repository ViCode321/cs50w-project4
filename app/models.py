from django.db import models

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    Gener = models.CharField(max_length=255)
    PerfilPhoto = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    Ubication = models.CharField(max_length=100, null=True, blank=True)
    Biography = models.TextField(null=True, blank=True)
    RegistrationDate = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    GroupID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.TextField(null=True, blank=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

class UserGroup(models.Model):
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Publication(models.Model):
    PublicationID = models.AutoField(primary_key=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Content = models.TextField()
    PublicationDate = models.DateTimeField(auto_now_add=True)

class Coment(models.Model):
    ComentID = models.AutoField(primary_key=True)
    Publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Content = models.TextField()
    ComentDate = models.DateTimeField(auto_now_add=True)

class PrivateMessage(models.Model):
    MessageID = models.AutoField(primary_key=True)
    Transmitter = models.ForeignKey(Users, related_name='send_message', on_delete=models.CASCADE)
    Receptor = models.ForeignKey(Users, related_name='received_message', on_delete=models.CASCADE)
    Content = models.TextField()
    SendDate = models.DateTimeField(auto_now_add=True)
    Check = models.BooleanField(default=False)
