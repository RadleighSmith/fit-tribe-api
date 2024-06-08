from rest_framework import permissions

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.

    This permission class allows read-only access to any request (GET, HEAD, OPTIONS).
    Write permissions (POST, PUT, DELETE) are only allowed to the owner of the object.

    Methods:
        has_object_permission(request, view, obj): Determines if the request has permission to perform the action on the given object.
            - Allows read-only access for any request method listed in SAFE_METHODS (GET, HEAD, OPTIONS).
            - Allows write access only if the user making the request is the owner of the object.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object
        return obj.owner == request.user

    
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users (staff or superuser) to edit objects.

    This permission class allows read-only access to any request (GET, HEAD, OPTIONS).
    Write permissions (POST, PUT, DELETE) are only allowed to admin users, which are defined as users
    who have either the `is_staff` or `is_superuser` attribute set to True.

    Methods:
        has_permission(request, view): Determines if the request has permission to perform the action.
            - Allows read-only access for any request method listed in SAFE_METHODS (GET, HEAD, OPTIONS).
            - Allows write access only if the user making the request is either a staff member or a superuser.
    """
    def has_permission(self, request, view):
        # SAFE_METHODS are GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to admin users (either staff or superuser)
        return request.user and (request.user.is_staff or request.user.is_superuser)
