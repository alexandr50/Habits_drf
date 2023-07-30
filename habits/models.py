from django.contrib.auth import get_user_model
from django.db import models

from habits.validators import is_nice_validator, reward_and_is_nice_validator,  is_to_long


class Habit(models.Model):
    ONE_A_DAY = 'раз в день'
    ONE_A_TWO_DAYS = 'раз в два дня'
    ONE_A_THREE_DAYS = 'раз в три дня'
    ONE_A_FOUR_DAYS = 'раз в четыре дня'
    ONE_A_FIVE_DAYS = 'раз в пять дней'
    ONE_A_SIX_DAYS = 'раз в шесть дней'
    ONE_A_WEEK = 'раз в неделю'

    INTERVAL_CHOICES = (
        (ONE_A_DAY, 'раз в день'),
        (ONE_A_TWO_DAYS, 'раз в два дня'),
        (ONE_A_THREE_DAYS, 'раз в три дня'),
        (ONE_A_FOUR_DAYS, 'раз в четыре дня'),
        (ONE_A_FIVE_DAYS, 'раз в пять дней'),
        (ONE_A_SIX_DAYS, 'раз в шесть дней'),
        (ONE_A_WEEK, 'раз в неделю')
    )

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='владелец')
    place = models.CharField(max_length=50, verbose_name='место')
    moment = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    reward = models.CharField(max_length=50, verbose_name='вознаграждение', blank=True, null=True)
    interval = models.CharField(choices=INTERVAL_CHOICES, default=ONE_A_DAY, verbose_name='периодичность выполнения')
    run_time = models.IntegerField(default=120, verbose_name='время выполнения в секундах', validators=[is_to_long])
    is_published = models.BooleanField(default=False, verbose_name='опубликованно')


    def __str__(self):
        return f'я буду {self.action} в {self.moment} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        reward_and_is_nice_validator(self)


class RelatedHabit(models.Model):
    habit = models.OneToOneField(Habit, on_delete=models.CASCADE, verbose_name='связанная привычка')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки',
                                  validators=[is_nice_validator, ])


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
