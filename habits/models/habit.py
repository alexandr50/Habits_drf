from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models


class Habit(models.Model):
    ONE_A_DAY = 'раз в день'
    TWO_DAYS = 'раз в два дня'
    THREE_DAYS = 'раз в три дня'
    FOUR_DAYS = 'раз в четыре дня'
    FIVE_DAYS = 'раз в пять дней'
    SIX_DAYS = 'раз в шесть дней'
    ONE_A_WEEK = 'раз в неделю'

    INTERVAL_CHOICES = (
        (ONE_A_DAY, 'раз в день'),
        (TWO_DAYS, 'раз в два дня'),
        (THREE_DAYS, 'раз в три дня'),
        (FOUR_DAYS, 'раз в четыре дня'),
        (FIVE_DAYS, 'раз в пять дней'),
        (SIX_DAYS, 'раз в шесть дней'),
        (ONE_A_WEEK, 'раз в неделю')
    )

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец')
    place = models.CharField(max_length=50, verbose_name='место')
    moment = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    reward = models.CharField(max_length=50, verbose_name='вознаграждение', blank=True, null=True)
    interval = models.CharField(choices=INTERVAL_CHOICES, default=ONE_A_DAY, verbose_name='периодичность выполнения')
    run_time = models.IntegerField(default=120, verbose_name='время выполнения в секундах')
    is_published = models.BooleanField(default=False, verbose_name='опубликованно')

    def __str__(self):
        return f'я буду {self.action} в {self.moment} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
