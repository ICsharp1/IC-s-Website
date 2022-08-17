from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
# Create your models here.


class Account(models.Model):
    email = models.EmailField(verbose_name='email',
                              max_length=60, unique=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='account')
    Dark = models.BooleanField(default=False, null=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.username
