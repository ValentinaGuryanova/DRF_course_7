from datetime import datetime
import os

import requests
from celery import shared_task

from habits.models import Habit


@shared_task
def send_message_to_bot() -> None:
    """ функция отправки сообщения в телеграм-бот
    chat_id: id чата
    message: передаваемое сообщение
    """
    token = os.getenv('TELEGRAM_BOT_API_KEY')
    obj = Habit.objects.all()

    for item in obj:
        if item.time == datetime.now().time():
            message = f'Привет {item.user}! Время {item.time}. Пора идти в {item.place} и сделать {item.action}. ' \
                      f'Это займет {item.duration} минут!'
            send_message_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={item.user.telegram_id}&text={message}"
            requests.get(send_message_url)
        else:
            print("Еще не пришло время выполнять привычку!")
