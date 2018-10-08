from rest_framework_json_api import serializers
from .models import Challenge, Tag, Attachment
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework_json_api.relations import ResourceRelatedField

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class AttachmentsSerializer(serializers.ModelSerializer):

    queryset = Attachment.objects.filter(active=True,)

    class Meta:
        model = Attachment
        fields = ('name', 'url', 'attachment_type')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('user', 'tags', 'attachments', 'created_at', 'updated_at', 'title', 'short_title', 'owner', 'difficulty',
            'challenge_type', 'priority', 'description', 'short_description',
            'extra_points', 'technical_notes', 'procedure', 'code_tips')

    queryset = Challenge.objects.filter(is_visible=True,)

    included_serializers = {
        'user':  UserSerializer,
        'tags': TagsSerializer,
        'attachments': AttachmentsSerializer,
    }

    user = ResourceRelatedField(
        queryset=User.objects
    )

    tags = ResourceRelatedField(
        queryset=Tag.objects,
        many=True,
    )

    attachments = ResourceRelatedField(
        queryset=Attachment.objects,
        many=True,
    )

    class JSONAPIMeta:
        included_resources = ['user', 'tags', 'attachments']

class TagGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'challenges')

    challenges = ResourceRelatedField(
        queryset=Challenge.objects,
        many=True,
    )

    included_serializers = {
        'challenges': ChallengeSerializer,
    }

    class JSONAPIMeta:
        included_resources = ['challenges',]
