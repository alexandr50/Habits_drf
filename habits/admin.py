from django.contrib import admin

from habits.models import Habit, RelatedHabit

admin.site.register(Habit)
admin.site.register(RelatedHabit)
