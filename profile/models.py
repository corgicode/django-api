from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone as tz
from django.apps import apps
import pytz
from django.conf import settings
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from usermanagement.models import User

class ProfileURL(models.Model):
    def __str__(self):
        return self.name

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250,)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Profile(models.Model):
    def __str__(self):
        return self.user.username

    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tagline = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    linkedin_url = models.CharField(max_length=255, blank=True)
    twitter_url = models.CharField(max_length=255, blank=True)
    github_url = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    blog = models.CharField(max_length=255, blank=True)
    public_repos = models.CharField(max_length=255, blank=True)
    hireable = models.BooleanField(default=False)
