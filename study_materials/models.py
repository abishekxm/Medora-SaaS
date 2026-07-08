from django.db import models


class StudyMaterial(models.Model):
    SUBJECT_CHOICES = [
        ("Physics", "Physics"),
        ("Chemistry", "Chemistry"),
        ("Biology", "Biology"),
    ]

    MATERIAL_CHOICES = [
        ("Notes", "Notes"),
        ("PYQ", "PYQ"),
        ("Book", "Book"),
    ]

    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    material_type = models.CharField(max_length=50, choices=MATERIAL_CHOICES)
    description = models.TextField(blank=True)
    pdf = models.FileField(upload_to="study_materials/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title