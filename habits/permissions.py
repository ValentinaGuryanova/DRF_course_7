from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Задаем права для владельца объекта """
    def has_object_permission(self, request, view, obj):

        if request.user == obj.habit_owner:
            return True

        return False


class IsPrizeOwner(BasePermission):
    """ Задаем права для владельца связанной привычки """
    def has_object_permission(self, request, view, obj):

        if request.user == obj.owner:
            return True

        return False