from django.shortcuts import render
from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitCreateSerializers


class HabitsListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializers


class HabitCreateView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializers


