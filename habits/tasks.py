from celery import shared_task


from habits.services import send_remainder
from users.models import User


@shared_task
def sending_remainder():
    users = User.objects.filter(is_active=True, chat_id__isnull=False)
    for user in users:
        send_remainder(user.chat_id)
