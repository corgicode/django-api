from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import password_validation


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(
        max_length=128,
        verbose_name='password',
        validators=[password_validation.validate_password]
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return self.username
