
import requests
from django.http import HttpResponse

from config.settings import TELEGRAM_ACCESS_TOKEN, TELEGRAM_CHAT_ID
from habits.models import Habit

bot_token = TELEGRAM_ACCESS_TOKEN
chat_id = TELEGRAM_CHAT_ID
get_id_url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
send_message_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'


def send_message_to_bot(chat_id, message):
    """ функция отправки сообщения в телеграм-бот
    chat_id: id чата
    message: передаваемое сообщение
    """

    params = {"chat_id": chat_id, "text": message}
    response = requests.get(send_message_url, params=params).json()
    return response


def create_message(id):
    """ Функция создания сообщения для отправки в телеграм-бот """

    habit = Habit.objects.get(id=id)

    user = habit.user
    time = habit.time
    action = habit.action
    place = habit.place
    duration = round(habit.duration.total_seconds() / 60)

    message = f'Привет {user}! Время {time}. Пора идти в {place} и сделать {action}. Это займет {duration} минут!'

    response = send_message_to_bot(chat_id, message)
    if habit.connected_habit or habit.prize:
        if habit.connected_habit:
            habit_is_good_id = habit.connected_habit.id
            habit_is_good = Habit.objects.get(id=habit_is_good_id)
            nice_time = round(habit_is_good.duration.total_seconds() / 60)
            nice_message = (f'Молодец! Ты выполнил {action}, за это тебе подарок {habit_is_good.action} '
                            f'в течение {nice_time} минут')

            time.sleep(10)
            nice_response = send_message_to_bot(chat_id, nice_message)

            return HttpResponse(nice_response)

        if habit.prize:
            prize_message = f'Молодец! Ты выполнил {action}, за это тебе подарок {habit.prize.description}'

            time.sleep(10)
            nice_response = send_message_to_bot(chat_id, prize_message)

            return HttpResponse(nice_response)
    return HttpResponse(response)


def get_bot_id():
    """ Получение данных чата """

    response = requests.get(get_id_url).json()
    return HttpResponse(response)
