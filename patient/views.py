from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    patient_list = Patient.objects.order_by('number')
    paginator = Paginator(patient_list, 10)
    page_obj = paginator.get_page(page)
    context = {'patient_list':page_obj}
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

def exercise(request, patient_number):
    patient = get_object_or_404(Patient, pk=patient_number)
    context = {'patient':patient}
    return render(request, 'patient/exercise.html', context)