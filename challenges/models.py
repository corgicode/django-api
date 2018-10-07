from django.db import models
from accounts.models import User

class Tag(models.Model):
    def __str__(self):
        return self.name

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250,)

class Challenge(models.Model):

    CHALLENGE_TYPES = (
        ('feature', 'Feature'),
        ('bug', 'Bug'),
        ('improvement', 'Improvement'),
        ('task', 'Task'),
        ('subtask', 'Sub Task'),
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    title = models.CharField(max_length=250,)
    short_title = models.CharField(max_length=250,)
    owner = models.CharField(max_length=250,)
    difficulty = models.CharField(max_length=250,)
    challenge_type = models.CharField(max_length=30, choices=CHALLENGE_TYPES, null=True, blank=True)
    priority = models.CharField(max_length=250)
    description = models.TextField()
    short_description = models.TextField()
    extra_points = models.TextField()
    technical_notes = models.TextField()
    procedure = models.TextField()
    code_tips = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='challenges')

class Attachment(models.Model):
    def __str__(self):
        return self.name

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250,)
    url = models.TextField()
    active = models.BooleanField(default=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.DO_NOTHING)

class Source(models.Model):
    def __str__(self):
        return self.name

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250,)
    url = models.TextField()
    active = models.BooleanField(default=True)
    challenge = models.ForeignKey(Challenge, related_name='sources', on_delete=models.DO_NOTHING)
