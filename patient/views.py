from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
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
    exercises = Exercise.objects.filter(part=part, type=type)
    exercise_list = ExerciseList.objects.filter(patient=patient_id)
    context = {'patient':patient, 'part':part, 'type':type, 'exercises':exercises, 'exercise_list':exercise_list}
    return render(request, 'patient/exercise_add.html', context)

def exercise_form(request, patient_id, part, type, exercise):
    patient = get_object_or_404(Patient2, pk = patient_id)
    exercise = get_object_or_404(Exercise, pk=exercise)
    exercise_list = ExerciseList.objects.filter(patient=patient_id)
    if request.method == 'POST':
        form = ExerciseAddForm(request.POST)
        if form.is_valid():
            exercise_list = form.save(commit=False)
            exercise_list.exercise = exercise
            exercise_list.patient = patient
            exercise_list.save()
            return redirect('patient:exercise_add', patient_id=patient_id, part=part, type=type)
    else:
        form = ExerciseAddForm(instance=ExerciseList())

    context={'patient':patient, 'exercise':exercise, 'form':form, 'exercise_list':exercise_list}
    return render(request, 'patient/exercise_form.html', context)

def rom(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    context = {'patient':patient}
    return render(request, 'patient/rom.html', context)

def rom_form(request, patient_id, part):
    patient = get_object_or_404(Patient2, pk=patient_id)
    if part=='경추':
        part = get_object_or_404(Part, pk=part)
        if request.method == 'POST':
            form = NeckTrunkForm(request.POST)
            if form.is_valid():
                rom = form.save(commit=False)
                rom.patient = patient
                rom.part = part
                rom.save()
                return redirect('patient:exercise_add', patient_id=patient_id, part=part, type=type)
        else:
            form = NeckTrunkForm(instance=ExerciseList())

        context={'patient':patient, 'part':part, 'form':form}
        return render(request, 'patient/rom_form.html', context)

    