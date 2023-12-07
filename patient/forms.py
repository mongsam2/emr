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
        model = NeckTrunck
        fields = ['date', 'flexion', 'extension', 'left_bending', 'right_bending', 'left_rotation', 'right_rotation']

class ShoulderHipForm(forms.ModelForm):
    class Meta:
        model = ShoulderHip2
        fields = ['date', 'flexion_L', 'flexion_R', 'extension_L', 'extension_R', 'lateral_rotation_L', 'lateral_rotation_R', 'medial_rotation_L', 'medial_rotation_R', 'abduction_L', 'abduction_R', 'adduction_L', 'adduction_R']

class ElbowForm(forms.ModelForm):
    class Meta:
        model = Elbow2
        fields = ['date', 'flexion_L', 'flexion_R' ,'extension_L','extension_R', 'pronation_L','pronation_R', 'supination_L', 'supination_R']

class KneeForm(forms.ModelForm):
    class Meta:
        model = Knee2
        fields = ['date', 'flexion_L', 'flexion_R', 'extension_L', 'extension_R']
    
class WristForm(forms.ModelForm):
    class Meta:
        model = Wrist2
        fields = ['date', 'flexion_L', 'flexion_R', 'extension_L', 'extension_R', 'ulnar_deviation_L', 'ulnar_deviation_R', 'radial_deviation_L', 'radial_deviation_R']

class AnkleForm(forms.ModelForm):
    class Meta:
        model = Ankle2
        fields = ['date', 'flexion_L', 'flexion_R', 'extension_L', 'extension_R', 'inversion_L', 'inversion_R', 'eversion_L', 'eversion_R'] 

        