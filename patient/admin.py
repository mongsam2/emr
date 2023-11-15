from django.contrib import admin

from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Patient, PatientAdmin)