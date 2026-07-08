from django.contrib import admin
from .models import StudyMaterial


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subject",
        "material_type",
        "uploaded_at",
    )

    list_filter = (
        "subject",
        "material_type",
    )

    search_fields = (
        "title",
        "description",
    )