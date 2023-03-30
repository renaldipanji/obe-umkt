from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import os

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nama = models.CharField(max_length=30, blank=True, verbose_name='Nama')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    forgot_password_token = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True )
