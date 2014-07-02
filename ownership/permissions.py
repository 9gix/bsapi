from rest_framework import permissions


class IsOwnerOrAdminElseReadOnly(permissions.BasePermission):
    """
    Permission that allow only owner and admin to edit it
    while others will only allowed to read.
    """

    def has_object_permissions(self, request, view, obj):
        """return true when any of the permission satisfied"""

        return (
            # allow any read-only request (e.g. GET, HEAD & OPTIONS)
            (request.method in permissions.SAFE_METHODS) or

            # allow Owner to make read-write request
            (request.user == obj.owner) or

            # allow Admin to make read-write request
            (request.user.is_staff)
        )
