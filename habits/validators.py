from rest_framework.exceptions import ValidationError


class IsNiceValidator:
    """валидация нп р=признак приятной привычки у связанной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_nice = dict(value).get(self.field)
        if not is_nice:
            raise ValidationError("Связанная привычка может быть тоьлко приятной")

# def is_nice_validator(value):
#     """валидация нп р=признак приятной привычки у связанной привычки"""
#
#     if value == False:
#         raise ValidationError("Связанная привычка может быть тоьлко приятной")
#     return value


class RewardAndIsNiceValidator:
    """Валидация на признак полезности и вознаграждение у одной привычки сразу"""

    def __init__(self, reward, is_nice):
        self.reward = reward
        self.is_nice = is_nice

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        is_nice = dict(value).get(self.is_nice)
        if is_nice + bool(reward) == 2:
            raise ValidationError('У привычки может быть или вознаграждение или признак приятной привычки')


class IsSoLong:
    """валидация продолжительности времени выполнения привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        run_time: int = dict(value).get(self.field)
        if run_time > 120:
            raise ValidationError('Время выполнения привычки должно быть не больше 120 секунд')
