from django import forms
from patient.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['number', 'name', 'front_resident', 'back_resident', 'phone']
        labels = {
            'number':'환자번호',
            'name':'환자이름',
            'front_resident':'주민번호 앞자리',
            'back_resident':'주민번호 뒷자리',
            'phone':'전화번호',
        }