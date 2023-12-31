from django.contrib import admin
from .models import *

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Patient, PatientAdmin)

class Patient2Admin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'id', 'front_resident', 'back_resident', 'phone')

admin.site.register(Patient2, Patient2Admin)

admin.site.register(ExerciseType)
admin.site.register(Part)
admin.site.register(Motion)

class ExerciseAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Exercise, ExerciseAdmin)

'''class RomAdmin(admin.ModelAdmin):
    search_fields = ['patient', 'date']
admin.site.register(Rom, RomAdmin)'''

class ExerciseListAdmin(admin.ModelAdmin):
    search_fields = ['patient', 'date']
    list_display = ('date', 'patient', 'exercise')
admin.site.register(ExerciseList, ExerciseListAdmin)


admin.site.register(NeckTrunck)
admin.site.register(ShoulderHip2)
admin.site.register(Elbow2)
admin.site.register(Knee2)
admin.site.register(Wrist2)
admin.site.register(Ankle2)


'''class NeckAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Neck, NeckAdmin)

class TrunkAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Trunk, TrunkAdmin)

class ShoulderAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Shoulder, ShoulderAdmin)

class ElbowAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Elbow, ElbowAdmin)

class WristAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Wrist, WristAdmin)

class HipAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Hip, HipAdmin)

class KneeAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Knee, KneeAdmin)

class AnkleAdmin(admin.ModelAdmin):
    search_fields = ['motion']
admin.site.register(Ankle, AnkleAdmin)'''