from django.core.management import BaseCommand

from habits.models import Habit
from habits.services import MyBot


class Command(BaseCommand):

    def handle(self, *args, **options):

        my_bot = MyBot()
        my_bot.send_message(f'Привет!')


