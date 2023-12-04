from django import forms
from patient.models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient2
        fields = ['id', 'name', 'front_resident', 'back_resident', 'phone']
        labels = {
            'id':'환자id',
            'name':'환자이름',
            'front_resident':'주민번호 앞자리',
            'back_resident':'주민번호 뒷자리',
            'phone':'전화번호',
        }

class Patient2Form(forms.ModelForm):
    class Meta:
        model = Patient2
        fields = ['name', 'front_resident', 'back_resident', 'phone']
        labels = {
            'name':'환자이름',
            'front_resident':'주민번호 앞자리',
            'back_resident':'주민번호 뒷자리',
            'phone':'전화번호',
        }
#----------------------------------------------------------------------------------------------------
class PatientAddForm(forms.ModelForm):
    class Meta:
        model = Patient2
        fields = ['name', 'front_resident', 'back_resident', 'phone', 'memo']
        labels = {
            'name':'환자이름',
            'front_resident':'주민번호 앞자리',
            'back_resident':'주민번호 뒷자리',
            'phone':'전화번호',
            'memo':'환자메모'
        }

class ExerciseAddForm(forms.ModelForm):
    class Meta:
        model = ExerciseList
        fields = ['date', 'set', 'count', 'time', 'weight', 'done']

class NeckTrunkForm(forms.ModelForm):
    class Meta:
        model = NeckTruck
        fields = ['date', 'flexion', 'extension', 'left_bending', 'right_bending', 'left_rotation', 'right_rotation']

    