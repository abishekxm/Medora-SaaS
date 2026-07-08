from django.contrib import admin
from .models import College

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'category', 'cutoff_mark', 'year')
    list_filter = ('state', 'category', 'year')
