from rest_framework.permissions import BasePermission


class IsRoomParticipant(BasePermission):
    """
    Only the doctor or patient belonging to the room
    can access it.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        return (
            obj.doctor.user == user or
            obj.patient.user == user
        )