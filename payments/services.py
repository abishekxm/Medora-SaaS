import razorpay
from django.conf import settings
from appointments.models import Appointment
from .models import Payment

def create_payment(patient, amount):
    return Payment.objects.create(patient=patient, amount=amount, status='pending')

def update_payment_status(payment_id, status, transaction_id=None):
    payment = Payment.objects.get(id=payment_id)
    payment.status = status
    if transaction_id:
        payment.transaction_id = transaction_id
    payment.save()
    return payment

def get_transaction_history(patient):
    return Payment.objects.filter(patient=patient).order_by('-created_at')

def create_razorpay_order(patient, appointment_id, amount):
    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )

    appointment = Appointment.objects.get(id=appointment_id)

    payment, created = Payment.objects.get_or_create(
        appointment=appointment,
        defaults={
            "patient": patient,
            "amount": amount,
            "status": "pending",
        },
    )

    if not created:
        payment.amount = amount
        payment.status = "pending"
        payment.save()

    order = client.order.create(
        {
            "amount": int(amount * 100),  # Razorpay uses paise
            "currency": "INR",
            "payment_capture": 1,
        }
    )

    payment.razorpay_order_id = order["id"]
    payment.save()

    return {
        "payment": payment,
        "order": order,
    }
