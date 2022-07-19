from logging_manager import eventslog
from rest_framework import permissions
from rest_framework.serializers import ValidationError

logger = eventslog.logger


class IsOwner(permissions.BasePermission):
    """
    This permission for allow only owner to edit data
    """

    def has_object_permission(self, request, view, obj):
        if not obj.id == request.user.id:
            logger.error(
                "{} - You do not have permission to perform this "
                "action. ".format(request.user)
            )
            raise ValidationError(
                {
                    "detail": """
                    You do not have permission to perform this action.
                    """
                }
            )
        return obj.id == request.user.id
