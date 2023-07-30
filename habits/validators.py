from rest_framework.validators import ValidationError


def is_nice_validator(value):
    """валидация нп р=признак приятной привычки у связанной привычки"""

    if value == False:
        raise ValidationError("Связанная привычка может быть тоьлко приятной")
    return value


def reward_and_is_nice_validator(obj):
    """Валидация на признак полезности и вознаграждение у одной привычки сразу"""

    if obj.is_nice + bool(obj.reward) == 2:
        raise ValidationError('У привычки может быть или вознаграждение или признак приятной привычки')


def is_to_long(run_time):
    if run_time > 120:
        raise ValidationError('Время выполнения привычки должно быть не больше 120 секунд')