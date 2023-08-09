from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='testing@mail.com', telegram='@testing', password="123"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {
            'owner': self.user.id,
            'place': "Kitchen",
            'moment': '20:00:00',
            'action': "Drink some water",
            'is_nice': False,
            'interval': 'раз в день',
            'run_time': 120,
            'is_published': True
        }

        response = self.client.post(
            '/habits/create/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(Habit.objects.all().count(), 1)
        self.assertEqual(Habit.objects.all().first().owner.email, 'testing@mail.com')

    def test_delete_habit(self):
        data = {
            'owner': self.user,
            'place': "Kitchen",
            'moment': '20:00:00',
            'action': "Drink some water",
            'is_nice': False,
            'interval': 'раз в день',
            'run_time': 120,
            'is_published': True
        }
        habit = Habit.objects.create(**data)

        response = self.client.delete(
            f'/habits/delete/{habit.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(Habit.objects.all().count(), 0)
        self.assertFalse(Habit.objects.filter(id=habit.id).exists())

    def test_update_habit(self):
        data = {
            'owner': self.user,
            'place': "Kitchen",
            'moment': '20:00:00',
            'action': "Drink some water",
            'is_nice': False,
            'interval': 'раз в день',
            'run_time': 120,
            'is_published': True
        }

        habit = Habit.objects.create(**data)

        data_for_update = {
            'owner': self.user.pk,
            'place': "Room",
            'moment': '20:00:00',
            'action': "Drink some water",
            'is_nice': False,
            'interval': 'раз в день',
            'run_time': 120,
            'is_published': True
        }

        response = self.client.put(
            f'/habits/update/{habit.pk}/',
            data=data_for_update,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Habit.objects.all().count(), 1)
        self.assertEqual(Habit.objects.all().first().place, 'Room')
