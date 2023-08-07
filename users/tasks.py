from celery import shared_task

from users.models import User
from users.sevices import get_new_user_chat_id, set_new_user_chat_id, get_welcome

@shared_task
def get_updates_bot():
    users = User.objects.filter(is_active=True, chat_id__isnull=True)
    if users:
        for user in users:
            chat_id = get_new_user_chat_id(user.telegram)
            if chat_id:
                set_new_user_chat_id(chat_id, user.telegram)
                get_welcome(chat_id)