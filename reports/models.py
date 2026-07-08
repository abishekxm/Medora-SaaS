from django.db import models
from django.conf import settings

class Report(models.Model):
    REPORT_TYPES = [
        ('appointment', 'Appointment Report'),
        ('doctor', 'Doctor Report'),
        ('patient', 'Patient Report'),
        ('analytics', 'Analytics'),
    ]
    
    title = models.CharField(max_length=255)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.report_type})"
