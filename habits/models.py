from datetime import timedelta

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Prize(models.Model):
    """ Модель награды """

    name = models.CharField(max_length=100, verbose_name='название награды')
    description = models.TextField(**NULLABLE, verbose_name='описание награды')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'награда'
        verbose_name_plural = 'награды'
        ordering = ('name',)


class Habit(models.Model):
    """ Модель привычки """

    PERIOD_DAILY = 'ежедневно'
    PERIOD_WEEKLY = 'еженедельно'

    PERIOD_CHOICES = (
        (PERIOD_DAILY, 'ежедневно'),
        (PERIOD_WEEKLY, 'еженедельно'),
    )

    user = models.CharField(max_length=50, verbose_name='пользователь')
    name = models.CharField(max_length=100, verbose_name='название привычки')
    place = models.CharField(max_length=100, **NULLABLE, verbose_name='место выполнения привычки')
    time = models.TimeField(**NULLABLE, verbose_name='время выполнения привычки')
    action = models.CharField(max_length=100, verbose_name='действие привычки')
    habit_is_good = models.BooleanField(default=True, verbose_name='признак приятной привычки')
    connected_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default=PERIOD_DAILY,
                              verbose_name='периодичность привычки')
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE, **NULLABLE, verbose_name='приз')
    duration = models.DurationField(default=timedelta(minutes=2), verbose_name='продолжительность выполнения привычки')
    habit_is_public = models.BooleanField(default=True, verbose_name='признак публичной привычки')
    habit_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.name}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('name',)
