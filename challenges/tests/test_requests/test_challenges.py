from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from accounts.models import User
from challenges.models import Challenge
import sure
import json

class ChallengeApiTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.content_type = 'application/vnd.api+json'

    def test_challenge_create(self):
        """
        Ensure we get the correct challenge
        """
        user = User.objects.filter(username="codecorgi").first()

        challenge = Challenge.objects.create(user=user,
            title = 'Test Challenge',
            short_title = 'Test Challenge',
            owner = 'Gandalf',
            difficulty = '5',
            challenge_type = 'feature',
            priority = 'High',
            description = 'This is a description',
            short_description = 'This is shorter',
            extra_points = 'Put it on github',
            technical_notes = 'Use Django',
            procedure = 'Clone the code, and then run it locally',
            code_tips = 'Use a linter',
        )

        response = self.client.get(f'/services/api/challenges?pk={ challenge.id }',
                                   content_type=self.content_type)

        response.status_code.should.equal(200)

        response_data = json.loads(response.content)
        attributes = response_data['data'][0]['attributes']
        relationships = response_data['data'][0]['relationships']
        attributes['title'].should.equal(challenge.title)
