from django.urls import path

from habits.apps import HabitsConfig
from habits.services import get_bot_id
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PrizeCreateAPIView, PrizeListAPIView, HabitPublicListAPIView, PrizeRetrieveAPIView, \
    PrizeUpdatePIView, PrizeDestroyPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit_create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('public/', HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit_update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_change'),
    path('habit_delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),

    path('prize_create/', PrizeCreateAPIView.as_view(), name='prize_create'),
    path('prizes/', PrizeListAPIView.as_view(), name='prize_list'),
    path('prize/<int:pk>/', PrizeRetrieveAPIView.as_view(), name='prize_detail'),
    path('prize_update/<int:pk>/', PrizeUpdatePIView.as_view(), name='prize_change'),
    path('prize_delete/<int:pk>/', PrizeDestroyPIView.as_view(), name='prize_delete'),

    path('get_bot_id/', get_bot_id, name='get_bot_id'),
]
