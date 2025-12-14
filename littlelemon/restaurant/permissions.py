from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # Проверяем, что пользователь аутентифицирован
        return user.is_authenticated
