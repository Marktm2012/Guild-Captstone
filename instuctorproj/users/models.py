from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(default=timezone.now)
    email = models.EmailField()
    bio = models.TextField()
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name + ', ' + self.first_name