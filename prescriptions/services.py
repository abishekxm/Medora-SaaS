from .models import Prescription

def create_prescription(data, medicines):
    prescription = Prescription.objects.create(**data)
    prescription.medicines.set(medicines)
    return prescription

def get_patient_history(patient_id):
    return Prescription.objects.filter(patient_id=patient_id)

def get_doctor_history(doctor_id):
    return Prescription.objects.filter(doctor_id=doctor_id)
