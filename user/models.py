from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(default="Hey there, I am a cute dog!")
    # breed=models.CharField(default=None, max_length=10)
    image=models.ImageField(default='default.jpg', upload_to='dogpics')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('R', 'Rather Not Say'),
        ('U', 'Specify Gender')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    def __str__(self):
        return f'{self.user.username} Profile'
