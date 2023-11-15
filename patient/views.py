from django.shortcuts import render, get_object_or_404
from .models import Patient

# Create your views here.
def index(request):
    patient_list = Patient.objects.order_by('number')
    context = {'patient_list':patient_list}
    return render(request, 'patient/patient_list.html', context)

def detail(request, patient_number):
    patient = get_object_or_404(Patient, pk=patient_number)
    context = {'patient':patient}
    return render(request, 'patient/patient_detail.html', context)
