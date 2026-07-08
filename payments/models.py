from django.db import models
from django.conf import settings
from appointments.models import Appointment


class Payment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="payments",
        on_delete=models.CASCADE,
    )

    appointment = models.OneToOneField(
    Appointment,
    on_delete=models.CASCADE,
    related_name="payment",
    null=True,
    blank=True,
    
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending",
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
    )

    razorpay_order_id = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    razorpay_payment_id = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    razorpay_signature = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.id} - {self.patient}"