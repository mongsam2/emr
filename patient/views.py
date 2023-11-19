from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm

# Create your views here.
def index(request):
    patient_list = Patient.objects.order_by('number')
    context = {'patient_list':patient_list}
    return render(request, 'patient/patient_list.html', context)

def detail(request, patient_number):
    patient = get_object_or_404(Patient, pk=patient_number)
    context = {'patient':patient}
    return render(request, 'patient/patient_detail.html', context)

def patient_add(request):
    if request.method =='POST': # 저장하기 버튼을 눌렀을 경우
        form = PatientForm(request.POST) # 입력정보가 저장되어있는 폼
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('patient:index')
    else: #url로 접근할 경우 GET 방식으로 접근
        form = PatientForm()
    context = {'form':form}
    return render(request, 'patient/patient_add.html', context)