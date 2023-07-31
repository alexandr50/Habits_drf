from rest_framework import serializers

from habits.models import Habit
from habits.validators import IsSoLong, RewardAndIsNiceValidator


class HabitCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [IsSoLong(field='run_time'), RewardAndIsNiceValidator(reward='reward', is_nice='is_nice')]
