from rest_framework_json_api import serializers
from .models import Challenge
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework_json_api.relations import ResourceRelatedField

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('user', 'created_at', 'updated_at', 'title', 'short_title', 'owner', 'difficulty',
            'challenge_type', 'priority', 'description', 'short_description',
            'extra_points', 'technical_notes', 'procedure', 'code_tips')

    included_serializers = {
        'user':  UserSerializer,
    }

    user = ResourceRelatedField(
        queryset=User.objects
    )

    class JSONAPIMeta:
        included_resources = ['user',]
