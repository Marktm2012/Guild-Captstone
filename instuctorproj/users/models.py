from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    birthday = models.DateField(default=timezone.now)
    email = models.EmailField()
    bio = models.TextField()
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    # Boolean to decifer between student and teacher
    is_instructor = models.BooleanField(default=False)
    # enrollments to be added once instructapp models are created


    def __str__(self):
        return self.last_name + ', ' + self.first_name