from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsRelatedhabitOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.habit.owner == request.user