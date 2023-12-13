from django.contrib import admin

from habits.models import Habit, Prize


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """ Отражение привычек в админке """

    list_display = ('user', 'name', 'habit_is_public', 'habit_owner',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    """ Отражение наград в админке """

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)