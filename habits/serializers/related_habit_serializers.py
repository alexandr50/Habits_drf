from rest_framework import serializers

from habits.models import RelatedHabit
from habits.validators import IsNiceValidator


class RelatedHabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelatedHabit
        fields = ('action',)


class RelatedHabitCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelatedHabit
        fields = '__all__'
        validators = [IsNiceValidator(field='is_nice')]
