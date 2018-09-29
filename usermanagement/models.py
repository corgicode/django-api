from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.utils import timezone as tz
from django.apps import apps
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from safedelete.managers import SafeDeleteManager
import jwt

class JWT:

    @staticmethod
    def encode(payload):
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def decode(encoded):
        return jwt.decode(encoded, settings.SECRET_KEY)

class UserManager(SafeDeleteManager, BaseUserManager):
    def create_user(self, email, password=None, unusable_password=False, **kwargs):
        user = self.model(email=email, password=password, **kwargs)

        user.save(using=self._db, unusable_password=unusable_password)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class User(SafeDeleteModel, AbstractBaseUser):

    _safedelete_policy = SOFT_DELETE

    USERNAME_FIELD = 'username'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=128,
                                verbose_name='password',
                                validators=[password_validation.validate_password])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.TextField(blank=True, null=True)
    heroImage = models.TextField(blank=True, null=True)
    github_id = models.TextField(max_length=255, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):

        if self.tracker.has_changed('email'):
            self.email = self.email.lower()

        if kwargs.get("unusable_password"):
            self.set_unusable_password()

        self.full_clean(exclude=["id"])

        if self.tracker.has_changed('password') and not kwargs.get("unusable_password"):
            self.set_password(self.password)

        kwargs.pop("unusable_password", None)

        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def generate_profile_edit_token(self):
        return JWT.encode({'user_id': self.id,
                           'token': default_token_generator.make_token(self)})

    def get_full_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def profile_url(self):
        return f'{settings.FRONTEND_DOMAIN}/profile/{ self.username }'

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def old_password(self):
        pass
