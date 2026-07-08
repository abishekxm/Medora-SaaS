from django.db import models
from django.conf import settings

class Notification(models.Model):
    TYPES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('in-app', 'In-App'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=10, choices=TYPES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notification_type} - {self.user.username}"
