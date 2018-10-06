from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from accounts.models import User
from profile.models import Profile
import sure
import json

class ProfileApiTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.content_type = 'application/vnd.api+json'

    def test_profile_create_with_user(self):
        """
        Ensure we get the correct profile
        """
        user = User.objects.create(username="husky")

        profile = Profile.objects.create(user=user, bio="Woof!")

        response = self.client.get("/services/api/profiles",
                                   content_type=self.content_type)

        response.status_code.should.equal(200)

        response_data = json.loads(response.content)
        attributes = response_data['data'][0]['attributes']
        relationships = response_data['data'][0]['relationships']
        attributes['bio'].should.equal(profile.bio)
        relationships['user']['data']['id'].should.equal(str(user.id))
