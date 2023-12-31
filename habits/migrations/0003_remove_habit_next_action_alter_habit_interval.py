# Generated by Django 4.2.3 on 2023-08-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='next_action',
        ),
        migrations.AlterField(
            model_name='habit',
            name='interval',
            field=models.CharField(choices=[('раз в день', 'раз в день'), ('раз в два дня', 'раз в два дня'), ('раз в три дня', 'раз в три дня'), ('раз в четыре дня', 'раз в четыре дня'), ('раз в пять дней', 'раз в пять дней'), ('раз в шесть дней', 'раз в шесть дней'), ('раз в неделю', 'раз в неделю')], default='раз в день', verbose_name='периодичность выполнения'),
        ),
    ]
