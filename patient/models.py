from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    number = models.IntegerField(primary_key=True) #고유번호
    name = models.CharField(max_length=10) # 이름
    front_resident = models.CharField(max_length=10) # 앞 주민번호
    back_resident = models.CharField(max_length=10) # 뒤 주민번호
    phone = models.CharField(max_length=30)

#---------------------------------------------------------------------------------

class Patient2(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    name = models.CharField(max_length=10)
    front_resident = models.CharField(max_length=8)
    back_resident = models.CharField(max_length=1)
    phone = models.CharField(max_length=30)

class ExercisePart(models.Model):
    part = models.CharField(primary_key=True, max_length=20)

class ExerciseType(models.Model):
    type = models.CharField(primary_key=True, max_length=20)

class Exercise(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    part = models.ForeignKey(ExercisePart, on_delete=models.CASCADE)
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

class ExerciseList(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    count = models.IntegerField()
    set = models.IntegerField()
    time = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

