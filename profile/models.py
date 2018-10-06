from django.db import models
from accounts.models import User
from api import settings

class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        verbose_name="user",
        on_delete=models.DO_NOTHING
    )
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
    name = models.CharField(max_length=255, blank=True)
    avatar_url = models.TextField(null=True)
    hero_image_url = models.TextField(null=True)
    private = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("user",)

    def __str__(self):
        return self.user.username

class ProfileURL(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile URLs"
        verbose_name_plural = "Profile URLs"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250,)
    description = models.TextField(blank=True)
    url = models.TextField(null=True,)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='urls')