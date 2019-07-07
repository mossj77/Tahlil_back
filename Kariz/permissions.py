from rest_framework.permissions import BasePermission

class dashboardpermission(BasePermission):
    def has_permission(self, request, view):
        return False


