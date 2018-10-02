from django.db import migrations, models
from api.utils import id_generator

def create_codecorgi_profile(apps, schema_editor):
    User = apps.get_model('usermanagement', 'User')
    Profile = apps.get_model('profile', 'Profile')

    corgiUser = User.objects.create(
        password=id_generator(),
        email='woof@codecorgi.co',
        is_verified=True,
        is_admin=True,
        name='corginson',
        username='codecorgi',
        avatar='https://raw.githubusercontent.com/corgicode/frontend-react/dev/src/assets/images/logo-square-hover.png',
        heroImage='https://raw.githubusercontent.com/corgicode/frontend-react/dev/src/assets/images/hero-image.jpg',
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
        public_repos = '',
        hireable = False,
        user = corgiUser,
    )

def delete_codecorgi_profile(apps, schema_editor):
    User = apps.get_model('usermanagement', 'User')
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
