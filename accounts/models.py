from django.contrib.auth.models import AbstractUser
from django.db import models

from utils import get_file_path

# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    photo = models.FileField(upload_to=get_file_path)
    birthday = models.DateField(null=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        swappable = 'AUTH_USER_MODEL'


