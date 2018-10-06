from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from accounts.models import User
import sure
import json


class UserApiTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.content_type = 'application/vnd.api+json'

    def test_patient_current_user_get(self):
        """
        Ensure we get a user.
        """
        response = self.client.get("/services/api/users",
                                   content_type=self.content_type)

        response.status_code.should.equal(200)

        response_data = json.loads(response.content)
        attributes = json.loads(response.content)['data'][0]['attributes']
        attributes['username'].should.equal('codecorgi')
