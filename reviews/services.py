from .models import Review

def create_or_update_review(patient, doctor, data):
    review, created = Review.objects.update_or_create(
        patient=patient,
        doctor=doctor,
        defaults=data
    )
    return review

def get_doctor_reviews(doctor_id):
    return Review.objects.filter(doctor_id=doctor_id)
