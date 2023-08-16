from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    username = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.user.username}'s Account"
