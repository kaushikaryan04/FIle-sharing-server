from rest_framework.permissions import IsAdminUser , IsAuthenticated

class IsSuperUser(IsAuthenticated ,IsAdminUser) :
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_superuser)