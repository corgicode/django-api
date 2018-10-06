from rest_framework_json_api import serializers
from .models import Profile, ProfileURL
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework_json_api.relations import ResourceRelatedField

class ProfileURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileURL
        fields = ('name', 'description', 'url',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'urls', 'bio', 'tagline', 'location', 'linkedin_url', 'hero_image_url',
            'name', 'avatar_url', 'twitter_url', 'github_url', 'company', 'blog', 'public_repos', 'hireable')

    included_serializers = {
        'user': UserSerializer,
        'urls':  ProfileURLSerializer,
    }

    user = ResourceRelatedField(
        queryset=User.objects
    )

    urls = ResourceRelatedField(
        queryset=ProfileURL.objects,
        many=True,
    )

    class JSONAPIMeta:
        included_resources = ['user', 'urls']

