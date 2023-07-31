from django.db import models

from habits.models import Habit


class RelatedHabit(models.Model):
    habit = models.OneToOneField(Habit, on_delete=models.CASCADE, verbose_name='связанная привычка')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки')


    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'связанная привыка'
        verbose_name_plural = 'связанные привычки'

    def save(self, *args, **kwargs):
        habit = Habit.objects.filter(id=self.habit_id).first()
        if habit.is_nice or habit.reward:
            raise Exception('Вы не можете создать связанную привычку так как уже получили вознаграждение или привычка уже приятная')
        else:
            super().save(*args, **kwargs)