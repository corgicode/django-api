# Generated by Django 2.1.2 on 2018-10-06 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tagline', models.CharField(blank=True, max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('linkedin_url', models.CharField(blank=True, max_length=255)),
                ('twitter_url', models.CharField(blank=True, max_length=255)),
                ('github_url', models.CharField(blank=True, max_length=255)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('blog', models.CharField(blank=True, max_length=255)),
                ('public_repos', models.CharField(blank=True, max_length=255)),
                ('hireable', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='ProfileURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('url', models.TextField(null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profile.Profile')),
            ],
        ),
    ]
