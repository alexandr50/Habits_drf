from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit, RelatedHabit
from users.models import User


class RelatedHabitsTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='testing@mail.com', telegram='@testing', password="123"
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place="Kitchen",
            moment='20:00:00',
            action="Drink some water",
            is_nice=False,
            interval='раз в день',
            run_time=120,
            is_published=True
        )

    def test_create_related_habit(self):
        data = {
            'habit': self.habit.pk,
            'action': 'drink some juice',
            'is_nice': True
        }

        response = self.client.post(
            '/habits/related_habits/create/',
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RelatedHabit.objects.all().count(), 1)
        self.assertEqual(RelatedHabit.objects.all().first().action, 'drink some juice')

    def test_delete_related_habit(self):
        data = {
            'habit': self.habit,
            'action': 'drink some juice',
            'is_nice': True
        }
        related_habit = RelatedHabit.objects.create(**data)

        response = self.client.delete(
            f'/habits/related_habits/delete/{related_habit.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(RelatedHabit.objects.all().count(), 0)
        self.assertFalse(RelatedHabit.objects.filter(id=related_habit.id).exists())
