from .models import Notification

def create_notification(user, notification_type, message):
    return Notification.objects.create(user=user, notification_type=notification_type, message=message)

def mark_as_read(notification_id):
    Notification.objects.filter(id=notification_id).update(is_read=True)
