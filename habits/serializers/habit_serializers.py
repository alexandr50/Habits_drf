from rest_framework import serializers

from habits.models import Habit, RelatedHabit
from habits.serializers.related_habit_serializers import RelatedHabitSerializers
from habits.validators import IsSoLong, RewardAndIsNiceValidator


class HabitCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ("place", "moment", "action", "is_nice", "reward", "interval", "run_time", "owner")
        validators = [IsSoLong(field='run_time'), RewardAndIsNiceValidator(reward='reward', is_nice='is_nice')]


class HabitListSerializers(serializers.ModelSerializer):
    related_habit = RelatedHabitSerializers(read_only=True, many=False)

    def get_related_habit(self, habit):
        if RelatedHabit.objects.get(habit=habit).exists():
            return True
        return False

    class Meta:
        model = Habit
        fields = ("id", "place", "moment", "action", "is_nice", "reward",
                  "interval", "run_time", "owner", 'related_habit')
