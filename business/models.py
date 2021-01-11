from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.utils import timezone
from django.urls import reverse

class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    is_justuser = models.BooleanField(default=False)

class Businessuser(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    about_business = models.TextField(default='')
    code = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.author.username} Business' 
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.jpg', upload_to='profilepics')
    location = models.CharField(max_length=150, default='update me')
    facebook = models.CharField(max_length=100, blank=True, default='#')
    instagram = models.CharField(max_length=100, blank=True, default='#')
    twitter = models.CharField(max_length=100, blank=True, default='#')
    def __str__(self):
        return f'{self.user.username} Profile' 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_photo.path)
        if img.height > 300 and img.width > 300:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)


class BusinessComment(models.Model):
    code = models.CharField(max_length=300)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.message


    







