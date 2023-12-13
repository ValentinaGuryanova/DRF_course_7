from rest_framework import generics


from users.models import User
# from users.permissions import IsOwner, IsSuperuser
from users.serializers import UserSerializer, AnyUserSerializer
# from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    """ Класс для создания пользователя """

    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """ Класс для вывода списка пользователей """

    serializer_class = AnyUserSerializer
    queryset = User.objects.all()

    # permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс для вывода одного пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Класс для изменения пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # permission_classes = [IsAuthenticated, IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Класс для удаления пользователя """

    queryset = User.objects.all()

    # permission_classes = [IsAuthenticated, IsOwner | IsSuperuser]