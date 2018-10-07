from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from accounts.models import User
from challenges.models import Challenge, Tag, Attachment, Source
import sure
import json
import pdb

class ChallengeApiTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.content_type = 'application/vnd.api+json'

    def get_sample_challenge(self, user=None, tags=None):
        if user is None:
            user = User.objects.filter(username="codecorgi").first()

        challenge = Challenge.objects.create(
            user=user,
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

        if not tags is None:
            challenge.tags.set(tags)

        return challenge


    def test_challenge_create(self):
        """
        Ensure we get the correct challenge
        """
        challenge = self.get_sample_challenge()

        response = self.client.get(f'/services/api/challenges?pk={ challenge.id }',
                                   content_type=self.content_type)

        response.status_code.should.equal(200)

        response_data = json.loads(response.content)
        attributes = response_data['data'][0]['attributes']
        attributes['title'].should.equal(challenge.title)

    def test_challenge_create_with_tags(self):
        """
        Ensure we get the correct tags information with a challenge
        """
        tag1 = Tag.objects.create(name='Javascript')

        challenge = self.get_sample_challenge(tags=[ tag1 ])

        response = self.client.get(f'/services/api/challenges?pk={ challenge.id }',
                                   content_type=self.content_type)

        response.status_code.should.equal(200)

        response_data = json.loads(response.content)
        attributes = response_data['data'][0]['attributes']
        included = response_data['included']

        attributes['title'].should.equal(challenge.title)

        [item for item in included if item.get('type') == 'tags'][0]['attributes']['name'].should.equal(tag1.name)

    def test_challenge_create_with_source(self):
        """
        Ensure we get the correct sources information with the challenge
        """
        challenge = self.get_sample_challenge()
        source = Source.objects.create(
            challenge=challenge,
            name='github',
            url='https://github.com/corgicode'
        )

        response = self.client.get(f'/services/api/challenges?pk={ challenge.id }',
                                   content_type=self.content_type)

        response.status_code.should.equal(200)

        response_data = json.loads(response.content)
        included = response_data['included']

        [item for item in included if item.get('type') == 'sources'][0]['attributes']['name'].should.equal(source.name)

    def get_challenges_with_tag_name(self):
        """
        Ensure we get the correct challenge
        """
        tag = Tag.objects.create(name='testTag')

        challenge1 = self.get_sample_challenge(tags=[ tag ])
        challenge2 = self.get_sample_challenge(tags=[ tag ])

        response = self.client.get(f'/services/api/tags?pk={ tag.name }',
                                   content_type=self.content_type)

        response.status_code.should.equal(200)

        response_data = json.loads(response.content)
        attributes = response_data['data'][0]['attributes']
        included = response_data['included']

        attributes['name'].should.equal(tag.name)

        len([item for item in included if item.get('type') == 'challenge']).should.equal(2)
