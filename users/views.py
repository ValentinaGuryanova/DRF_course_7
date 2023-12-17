from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.permissions import IsOwner
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Класс для создания пользователя """

    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """ Класс для вывода списка пользователей """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс для вывода одного пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Класс для изменения пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Класс для удаления пользователя """

    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, IsOwner]
