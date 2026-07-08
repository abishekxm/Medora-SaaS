from rest_framework import permissions

class IsPatientOrDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user or obj.doctor.user == request.user