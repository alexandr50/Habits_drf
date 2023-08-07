from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.pagination import PaginationsHabits
from habits.serializers import HabitCreateSerializers
from habits.serializers.habit_serializers import HabitListSerializers
from users.permissions import IsOwner


class HabitsListView(generics.ListAPIView):
    # queryset = Habit.objects.all()
    serializer_class = HabitListSerializers
    pagination_class = PaginationsHabits
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(is_published=True)


class HabitCreateView(generics.CreateAPIView):
    """"Создание основной привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializers
    permission_classes = [IsAuthenticated]


class HabitUpdateView(generics.UpdateAPIView):
    """"Изменение основной привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializers
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteView(generics.DestroyAPIView):
    """"Удаление основной привычки"""

    queryset = Habit.objects.all()
    # serializer_class = HabitCreateSerializers
    permission_classes = [IsAuthenticated, IsOwner]
