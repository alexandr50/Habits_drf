from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def test_create_user(self):
        data = {
            'email': 'testing@mail.com', 'telegram': '@testing', 'password': "123"
        }
        response = self.client.post(
            '/users/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(User.objects.all().first().email, 'testing@mail.com')
        self.assertEqual(User.objects.all().count(), 1)
