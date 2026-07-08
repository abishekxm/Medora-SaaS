from .models import Doctor

def verify_doctor(doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    doctor.is_verified = True
    doctor.save()
    return doctor