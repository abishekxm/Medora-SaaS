from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Prescription
from .serializers import PrescriptionSerializer
from .permissions import IsDoctorOrReadOnly


from rest_framework import permissions

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        # Implementation for generating/downloading PDF would go here
        return Response({"message": "Download initiated"})
