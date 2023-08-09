import os

import django
from django.test import TestCase

from users.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()


class Test(TestCase):

    def test_user_services(self):
        data = {
            'email': 'someemail@mail.ru',
            'telegram': '@ElizavetaSergeevnaMaslova',
            'password': '123qwe'
        }
        user = User.objects.create(**data)
        self.assertEqual(user.email, 'someemail@mail.ru')
