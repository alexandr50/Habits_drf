from django.urls import path, include

from habits.views import HabitsListView, HabitCreateView

urlpatterns = [
    path('',  HabitsListView.as_view(), name='list_view'),
    path('create/',  HabitCreateView.as_view(), name='list_view'),

]