from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Count

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
        form = ExerciseAddForm()

    context={'patient':patient, 'exercise':exercise, 'form':form, 'exercise_list':exercise_list}
    return render(request, 'patient/exercise_form.html', context)

def rom(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    context = {'patient':patient}
    return render(request, 'patient/rom.html', context)

def rom_form(request, patient_id, part):
    model_dic = {'경추':NeckTrunck, '흉요추':NeckTrunck, '어깨':ShoulderHip2, '고관절':ShoulderHip2, '팔꿈치':Elbow2, '무릎':Knee2, '손목':Wrist2, '발목':Ankle2}
    part_model = get_object_or_404(Part, pk=part)
    model = model_dic[part].objects.filter(patient=patient_id, part=part_model)
    first = model_dic[part].objects.filter(patient=patient_id, part=part_model).order_by('-date').first()
    patient = get_object_or_404(Patient2, pk=patient_id)
    if part in ['경추', '흉요추']:
        if request.method == 'POST':
            form = NeckTrunkForm(request.POST)
            if form.is_valid():
                rom = form.save(commit=False)
                rom.patient = patient
                rom.part = part_model
                rom.save()
                return redirect('patient:rom_form', patient_id=patient_id, part=part)
        else:
            form = NeckTrunkForm()
        context={'patient':patient, 'part':part_model, 'form':form, 'model':model, 'first':first}
        return render(request, 'patient/rom_form.html', context)
    elif part in ['어깨', '고관절']:
        if request.method == 'POST':
            form = ShoulderHipForm(request.POST)
            if form.is_valid():
                rom = form.save(commit=False)
                rom.patient = patient
                rom.part = part_model
                rom.save()
                return redirect('patient:rom_form', patient_id=patient_id, part=part)
        else:
            form = ShoulderHipForm()
        context={'patient':patient, 'part':part_model, 'form':form, 'model':model, 'first':first}
        return render(request, 'patient/rom_form.html', context)
    else:
        dic = {'팔꿈치':ElbowForm, '무릎':KneeForm, '손목':WristForm, '발목':AnkleForm}
        if request.method == 'POST':
            form = dic[part](request.POST)
            if form.is_valid():
                rom = form.save(commit=False)
                rom.patient = patient
                rom.part = part_model
                rom.save()
                return redirect('patient:rom_form', patient_id=patient_id, part=part)
        else:
            form = dic[part]()
        context={'patient':patient, 'part':part_model, 'form':form, 'model':model, 'first':first}
        return render(request, 'patient/rom_form.html', context)

def data_index(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    context = {'patient':patient}
    return render(request, 'patient/data_index.html', context)

def data1(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    exercise_list = ExerciseList.objects.filter(patient=patient)
    
    part_group = exercise_list.values('exercise__part').annotate(part_count=Count('code'))
    data1 = [item['part_count'] for item in part_group]
    data1_list = [0]*6
    for i in range(len(data1)):
        data1_list[i] = data1[i]

    type_group = exercise_list.values('exercise__type').annotate(type_count=Count('code'))
    data1 = [item['type_count'] for item in type_group]
    data2_list = [0]*4
    for i in range(len(data1)):
        data2_list[i] = data1[i]

    context = {'patient':patient,'data1_list':data1_list, 'data2_list':data2_list}
    return render(request, 'patient/data1.html', context)

def data2(request, patient_id):
    patient = get_object_or_404(Patient2, pk=patient_id)
    context = {'patient':patient}
    return render(request, 'patient/data2.html',context)

def exercise_data(request, patient_id, part, type):
    patient = get_object_or_404(Patient2, pk=patient_id)
    part_model = get_object_or_404(Part, pk=part)
    type_model = get_object_or_404(ExerciseType, pk=type)
    exercises = Exercise.objects.filter(part=part, type=type)
    context = {'patient':patient, 'exercises':exercises, 'part':part, 'type':type}
    return render(request, 'patient/exercise_data.html', context)

def exercise_graph(request, patient_id, part, type, exercise):
    patient = get_object_or_404(Patient2, pk=patient_id)
    exercises = Exercise.objects.filter(part=part, type=type)
    exercise_list = ExerciseList.objects.filter(patient=patient, exercise=exercise).order_by('-date')[:5]
    date_list = ['']*len(exercise_list)
    set_list = [0]*len(exercise_list)
    count_list = [0]*len(exercise_list)
    weight_list = [0]*len(exercise_list)
    time_list = [0]*len(exercise_list)
    for i in range(len(exercise_list)):
        date_list[i] = exercise_list[i].date.strftime("%Y-%m-%d")
        set_list[i] = exercise_list[i].set
        count_list[i] = exercise_list[i].count
        weight_list[i] = exercise_list[i].weight
        time_list[i] = exercise_list[i].time
    context = {'patient':patient, 'exercise':exercise, 'set_list':set_list[::-1], 'count_list':count_list[::-1], 'weight_list':weight_list[::-1], 'time_list':time_list[::-1], 'date_list':date_list[::-1], 'exercises':exercises}
    return render(request, 'patient/exercise_graph.html', context)

def rom_graph(request, patient_id, part):
    model_dic = {'경추':NeckTrunck, '흉요추':NeckTrunck, '어깨':ShoulderHip2, '고관절':ShoulderHip2, '팔꿈치':Elbow2, '무릎':Knee2, '손목':Wrist2, '발목':Ankle2}
    patient = get_object_or_404(Patient2, pk=patient_id)
    model = model_dic[part]

    context = {'patient':patient}
    return render(request, 'patient/rom_graph', context)