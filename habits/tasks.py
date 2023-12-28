import requests
from celery import shared_task
from django.conf import settings

import habits
from config.settings import TELEGRAM_CHAT_ID, TELEGRAM_BOT_API_KEY
from habits.models import Habit

bot_token = TELEGRAM_BOT_API_KEY
telegram_id = TELEGRAM_CHAT_ID
get_id_url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
send_message_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'


@shared_task
def send_message_to_bot(habit_id):
    """ функция отправки сообщения в телеграм-бот
    chat_id: id чата
    message: передаваемое сообщение
    """
    habit = Habit.objects.get(id=habit_id)

    requests.post(
        url=f'{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
        data={
            'chat_id': habit.user.telegram_id,
            'text': habits.services.create_message
        }
    )
