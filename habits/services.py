import requests

from config import settings
from habits.models import Habit, RelatedHabit
from users.models import User

token = settings.TOKEN_BOT
chat_id = settings.CHAT_ID


def send_remainder(chat_id):
    user = User.objects.get(chat_id=chat_id)
    habits = Habit.objects.filter(owner=user)
    for habit in habits:
        print(habit)
        message = f"Привет, {user.telegram}, напоминаю что завтра у вас выполенние привычки: {habit}"
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.post(url)
        related_habit = RelatedHabit.objects.filter(habit=habit).first()
        if related_habit:
            print(related_habit)
            message = f"Не забудьте про приятную привычку{related_habit}"
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
            requests.post(url)
