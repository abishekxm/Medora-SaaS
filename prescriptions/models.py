from django.db import models
from django.conf import settings

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    dosage_instructions = models.TextField()

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='patient_prescriptions', on_delete=models.CASCADE)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='doctor_prescriptions', on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prescription {self.id} for {self.patient}"
