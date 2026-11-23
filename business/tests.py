
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BusinessHomeAPITests(APITestCase):

    def test_business_home_returns_welcome_message(self):
        url = reverse('business-home')

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['message'],
            'Welcome to Gas Daju Business API!'
        )
