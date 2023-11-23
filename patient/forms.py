from django import forms
from patient.models import Patient2

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
        fields = ['id', 'name', 'front_resident', 'back_resident', 'phone']
        labels = {
            'id':'환자id',
            'name':'환자이름',
            'front_resident':'주민번호 앞자리',
            'back_resident':'주민번호 뒷자리',
            'phone':'전화번호',
        }