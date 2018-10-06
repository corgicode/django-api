from rest_framework_json_api import serializers
from .models import Profile
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework_json_api.relations import ResourceRelatedField

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'user',)

    included_serializers = { 'user': UserSerializer }

    user = ResourceRelatedField(
        queryset=User.objects  # queryset argument is required
    )                              # except when read_only=True

    class JSONAPIMeta:
        included_resources = ['user',]

