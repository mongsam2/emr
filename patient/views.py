from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PatientForm, PatientAddForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    patient_list = Patient2.objects.order_by('id')
    paginator = Paginator(patient_list, 10)
    page_obj = paginator.get_page(page)
    context = {'patient_list':page_obj}
    return render(request, 'patient/patient_list.html', context)

def detail(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    context = {'patient':patient}
    return render(request, 'patient/patient_detail.html', context)

def patient_add(request):
    if request.method =='POST': # 저장하기 버튼을 눌렀을 경우
        form = PatientAddForm(request.POST) # 입력정보가 저장되어있는 폼
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('patient:index')
    else: #url로 접근할 경우 GET 방식으로 접근
        form = PatientAddForm()
    context = {'form':form}
    return render(request, 'patient/patient_add.html', context)

def patient_modify(request, patient_id):
    patient = get_object_or_404(Patient2, pk = patient_id)
    if request.method == 'POST':
        form = PatientAddForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('patient:detail', patient_id = patient.id)
    else:
        form = PatientAddForm(instance=patient)
    context = {'form':form}
    return render(request, 'patient/patient_add.html', context)
def exercise(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    exercise_list = ExerciseList.objects.filter(patient=patient_id)
    context = {'patient':patient, 'exercise_list':exercise_list}
    return render(request, 'patient/exercise.html', context)

def exercise_add(request, patient_id, part, type):
    patient = get_object_or_404(Patient2, pk=patient_id)
    part = get_object_or_404(Part, pk=part)
    type = get_object_or_404(ExerciseType, pk=type)
    exercises = Exercise.objects.filter(part='목', type='스트레칭')
    exercise_list = ExerciseList.objects.filter(patient=patient_id)
    context = {'patient':patient, 'part':part, 'type':type, 'exercises':exercises, 'exercise_list':exercise_list}
    return render(request, 'patient/exercise_add.html', context)

def rom(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    context = {'patient':patient}
    return render(request, 'patient/rom.html', context)