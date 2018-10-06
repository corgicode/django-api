from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import password_validation

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, password=password, **kwargs)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, password=password, username=username, is_admin=True)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

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

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
