# Generated by Django 4.2.3 on 2023-08-07 15:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='место')),
                ('moment', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=255, verbose_name='действие')),
                ('is_nice', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('reward', models.CharField(blank=True, max_length=50, null=True, verbose_name='вознаграждение')),
                ('interval', models.CharField(choices=[(datetime.timedelta(days=1), 'раз в день'), (datetime.timedelta(days=2), 'раз в два дня'), (datetime.timedelta(days=3), 'раз в три дня'), (datetime.timedelta(days=4), 'раз в четыре дня'), (datetime.timedelta(days=5), 'раз в пять дней'), (datetime.timedelta(days=6), 'раз в шесть дней'), (datetime.timedelta(days=7), 'раз в неделю')], default=datetime.timedelta(days=1), verbose_name='периодичность выполнения')),
                ('run_time', models.IntegerField(default=120, verbose_name='время выполнения в секундах')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликованно')),
                ('next_action', models.DateField(default=models.CharField(choices=[(datetime.timedelta(days=1), 'раз в день'), (datetime.timedelta(days=2), 'раз в два дня'), (datetime.timedelta(days=3), 'раз в три дня'), (datetime.timedelta(days=4), 'раз в четыре дня'), (datetime.timedelta(days=5), 'раз в пять дней'), (datetime.timedelta(days=6), 'раз в шесть дней'), (datetime.timedelta(days=7), 'раз в неделю')], default=datetime.timedelta(days=1), verbose_name='периодичность выполнения'), verbose_name='дата следующего выполнения')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
        migrations.CreateModel(
            name='RelatedHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255, verbose_name='действие')),
                ('is_nice', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('habit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_habit', to='habits.habit', verbose_name='главная привычка')),
            ],
            options={
                'verbose_name': 'связанная привыка',
                'verbose_name_plural': 'связанные привычки',
            },
        ),
    ]
