from rest_framework_json_api import serializers
from .models import Challenge, Tag, Source
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework_json_api.relations import ResourceRelatedField

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class SourcesSerializer(serializers.ModelSerializer):

    queryset = Source.objects.filter(active=True,)

    class Meta:
        model = Source
        fields = ('name', 'url')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('user', 'tags', 'sources', 'created_at', 'updated_at', 'title', 'short_title', 'owner', 'difficulty',
            'challenge_type', 'priority', 'description', 'short_description',
            'extra_points', 'technical_notes', 'procedure', 'code_tips')

    included_serializers = {
        'user':  UserSerializer,
        'tags': TagsSerializer,
        'sources': SourcesSerializer,
    }

    user = ResourceRelatedField(
        queryset=User.objects
    )

    tags = ResourceRelatedField(
        queryset=Tag.objects,
        many=True,
    )

    sources = ResourceRelatedField(
        queryset=Source.objects,
        many=True,
    )

    class JSONAPIMeta:
        included_resources = ['user', 'tags', 'sources']

