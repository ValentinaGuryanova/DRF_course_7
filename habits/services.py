from django_celery_beat.models import PeriodicTask, CrontabSchedule

from config import settings


def create_reminder(habit):
    """ Создание расписания и задачи """

    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_week='*' if habit.period == 'ежедневно' else '*/7',
        month_of_year='*',
        timezone=settings.TIME_ZONE
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'Habit Task - {habit.name}',
        task='habits.tasks.send_message_to_bot',
        args=[habit.id],
    )


def delete_reminder(habit):
    """ Удаление задачи """

    task_name = f'send_message_to_bot_{habit.id}'
    PeriodicTask.objects.filter(name=task_name).delete()


def update_reminder(habit):
    """ Обновление задачи """

    delete_reminder(habit)
    create_reminder(habit)
