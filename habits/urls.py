from django.urls import path

from habits.views import HabitsListView, HabitCreateView, HabitUpdateView, HabitDeleteView, RelatedHabitListView
from habits.views.related_habits_views import RelatedHabitCreateView, RelatedHabitDeleteView, RelatedHabitUpdateView

urlpatterns = [
    path('', HabitsListView.as_view(), name='list_view'),
    path('create/', HabitCreateView.as_view(), name='create_view'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>/', HabitDeleteView.as_view(), name='delete_view'),
    path('related_habits/', RelatedHabitListView.as_view(), name='list_view'),
    path('related_habits/create/', RelatedHabitCreateView.as_view(), name='create_view'),
    path('related_habits/update/<int:pk>/', RelatedHabitUpdateView.as_view(), name='update_view'),
    path('related_habits/delete/<int:pk>/', RelatedHabitDeleteView.as_view(), name='delete_view'),
]
