from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsOwnerAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["list", "retrieve"]:
            return True
        if obj.user != request.user:
            raise PermissionDenied(
                detail="You are not allowed to modify or delete this review."
            )
        return True
