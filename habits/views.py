from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit, Prize
from habits.paginators import HabitPrizePaginator
from habits.permissions import IsOwner, IsPrizeOwner
from habits.serializers import HabitSerializer, PrizeSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer
    # queryset = Habit.objects.all()

    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """

        new_habit = serializer.save()
        new_habit.habit_owner = self.request.user

        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """ Вывод списка привычек пользователя """

    serializer_class = HabitSerializer
    pagination_class = HabitPrizePaginator

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(habit_owner=self.request.user)
        return queryset


class HabitPublicListAPIView(generics.ListAPIView):
    """ Вывод списка публичных привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPrizePaginator

    permission_classes = [AllowAny]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(habit_is_public=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр информации об одной привычке """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Изменение привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """

    queryset = Habit.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]


class PrizeCreateAPIView(generics.CreateAPIView):
    """ Создание награды """

    serializer_class = PrizeSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """

        new_prize = serializer.save()
        new_prize.prize_owner = self.request.user

        new_prize.save()


class PrizeListAPIView(generics.ListAPIView):
    """ Вывод списка наград """

    serializer_class = PrizeSerializer

    permission_classes = [IsAuthenticated, IsPrizeOwner]
    # permission_classes = [AllowAny]

    pagination_class = HabitPrizePaginator

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Prize.objects.filter(prize_owner=self.request.user)
        return queryset


class PrizeRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр информации об одной награде """

    serializer_class = PrizeSerializer
    queryset = Prize.objects.all()

    permission_classes = [IsAuthenticated, IsPrizeOwner]


class PrizeUpdatePIView(generics.UpdateAPIView):
    """ Изменение награды """

    serializer_class = PrizeSerializer
    queryset = Prize.objects.all()

    permission_classes = [IsAuthenticated, IsPrizeOwner]


class PrizeDestroyPIView(generics.DestroyAPIView):
    """ Удаление награды """

    queryset = Prize.objects.all()

    permission_classes = [IsAuthenticated, IsPrizeOwner]