from datetime import datetime

import pytz
from celery import shared_task

from habits.models import Habit
from habits.services import create_message


@shared_task
def check_habits_daily():
    """ Проверка ежедневных привычек на выполнение """

    date_time_now = datetime.now()
    moscow_timezone = pytz.timezone('Europe/Moscow')
    date_now = date_time_now.astimezone(moscow_timezone)
    time_now = date_now.time()

    habits = Habit.objects.filter(time__hour=time_now.hour, time__minute=time_now.minute,
                                  period='ежедневно', habit_is_good=False)

    for habit in habits:
        create_message(habit.id)


@shared_task
def check_habits_weekly():
    """ Проверка еженедельных привычек на выполнение """

    date_time_now = datetime.now()
    moscow_timezone = pytz.timezone('Europe/Moscow')
    date_now = date_time_now.astimezone(moscow_timezone)
    time_now = date_now.time()

    habits = Habit.objects.filter(time__hour=time_now.hour, time__minute=time_now.minute,
                                  period='еженедельно', habit_is_good=False)

    for habit in habits:
        create_message(habit.id)