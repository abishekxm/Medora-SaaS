from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'license_number', 'is_verified')
    list_filter = ('is_verified', 'specialization')
    search_fields = ('user__username', 'license_number')