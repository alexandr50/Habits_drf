import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from users.models import User
import requests
from config import settings

token = settings.TOKEN_BOT
chat_id = settings.CHAT_ID



def get_new_user_chat_id(telegram):
    api_url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(api_url)
    data = response.json()
    if data['ok'] and data['result']:
        for update in data['result']:
            if 'message' in update and 'from' in update['message']:
                if telegram[1:] == update['message']['from']['username']:
                    chat_id = update['message']['from']['id']
                    return chat_id
    else:
        return None


def set_new_user_chat_id(chat_id, telegram):
    user = User.objects.get(telegram=telegram)
    user.chat_id = chat_id
    user.save()




def get_welcome(chat_id):
    user = User.objects.get(chat_id=chat_id)
    message = f"Приветсвую, {user.telegram}, здесь будут напоминания ваших привычек"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    request = requests.post(url)


