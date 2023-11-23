from django.contrib import admin

from .models import *

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Patient, PatientAdmin)

class Patient2Admin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Patient2, Patient2Admin)

class ExercisePartAdmin(admin.ModelAdmin):
    search_fields = ['part']
admin.site.register(ExercisePart, ExercisePartAdmin)

class ExerciseTypeAdmin(admin.ModelAdmin):
    search_fields = ['type']
admin.site.register(ExerciseType, ExerciseTypeAdmin)

class ExerciseAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Exercise, ExerciseAdmin)

class ExerciseListAdmin(admin.ModelAdmin):
    search_fields = ['date']
admin.site.register(ExerciseList, ExerciseListAdmin)