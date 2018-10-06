from django.db import migrations, models
from api.utils import id_generator

def create_codecorgi_profile(apps, schema_editor):
    User = apps.get_model('accounts', 'User')
    Profile = apps.get_model('profile', 'Profile')

    corgiUser = User.objects.create(
        password=id_generator(),
        email='woof@codecorgi.co',
        is_verified=True,
        is_admin=True,
        username='codecorgi',
    )

    Profile.objects.create(
        tagline = 'Woof Woof',
        bio = 'Coder\'s best friend',
        location = 'Brooklyn, NY',
        linkedin_url = 'https://www.linkedin.com/company/codecorgi',
        twitter_url = 'https://twitter.com/codecorgi',
        github_url = 'https://github.com/corgicode',
        company = 'codecorgi',
        blog = 'https://medium.com/@codecorgi',
        public_repos = 'https://github.com/code-corgi',
        hireable = False,
        user = corgiUser,
        name = 'Corginson',
        avatar_url = 'https://raw.githubusercontent.com/corgicode/frontend-react/dev/src/assets/images/logo-square-hover.png',
        hero_image_url = 'https://raw.githubusercontent.com/corgicode/frontend-react/dev/src/assets/images/hero-image.jpg',
    )

def delete_codecorgi_profile(apps, schema_editor):
    User = apps.get_model('accounts', 'User')
    Profile = apps.get_model('profile', 'Profile')

    corgiUser = User.objects.filter(email='woof@codecorgi.co').first()
    Profile.objects.filter(user_id=corgiUser.id).delete()
    corgiUser.delete()


class Migration(migrations.Migration):
    dependencies = [
       ('profile', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_codecorgi_profile, delete_codecorgi_profile),
    ]
