from django.db import models
import uuid
from django.utils import timezone
from .templatetags.patient_filter import back

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
    front_resident = models.CharField(max_length=6)
    back_resident = models.CharField(max_length=1)
    phone = models.CharField(max_length=30)
    memo = models.TextField(default='memo')

    def __str__(self):
        return self.name + ' ' + self.front_resident +' ' + back(self.back_resident) + ' ' + self.id[:2]


'''class ExerciseList(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    count = models.IntegerField(default=0)
    set = models.IntegerField(default=1)
    time = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)'''

#------------------ 부위 별 테이블 -----------------------------------------------------------------

'''class Neck(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)
    arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)

class Trunk(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)
    arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)

class Shoulder(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)
    arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)

class Elbow(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)
    arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)

class Wrist(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)
    arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)

class Hip(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)
    arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)

class Knee(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)
    arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)

class Ankle(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    motion = models.CharField(max_length=8)
    arom = models.IntegerField(default=0)
    other_arom = models.IntegerField(default=0)
    prom = models.IntegerField(default=0)
    other_prom = models.IntegerField(default=0)'''

#-------------- 운동 종류 ---------------------------------------------------

class ExerciseType(models.Model):
    type = models.CharField(primary_key=True, max_length=20)

class Part(models.Model):
    part = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return self.part

class Motion(models.Model):
    motion = models.CharField(primary_key=True, max_length=8)

class Exercise(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    link = models.URLField(default='https://blog.naver.com/smile86/221055278905')

'''class Rom(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    motion = models.ForeignKey(Motion, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    rom = models.IntegerField(default=0)
    other_rom = models.IntegerField(default=0)'''

class ExerciseList(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    count = models.IntegerField(default=0)
    set = models.IntegerField(default=1)
    time = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    done = models.BooleanField(default=False)

#------------------------------------------------------------------------------------------

class NeckTruck(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    flexion = models.IntegerField()
    extension = models.IntegerField()
    left_bending = models.IntegerField()
    right_bending = models.IntegerField()
    left_rotation = models.IntegerField()
    right_rotation = models.IntegerField()

class ShoulderHip(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    flexion = models.IntegerField()
    extension = models.IntegerField()
    lateral_rotation = models.IntegerField()
    medial_rotation = models.IntegerField()
    abduction = models.IntegerField()
    adduction = models.IntegerField()

class Elbow(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    flexion = models.IntegerField()
    extension = models.IntegerField()
    pronation = models.IntegerField()
    supination = models.IntegerField()

class Knee(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    flexion = models.IntegerField()
    extension = models.IntegerField()

class Wrist(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    flexion = models.IntegerField()
    extension = models.IntegerField()
    ulnar_deviation = models.IntegerField()
    radial_deviation = models.IntegerField()

class Ankle(models.Model):
    code = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = models.ForeignKey(Patient2, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    flexion = models.IntegerField()
    extension = models.IntegerField()
    inversion = models.IntegerField()
    eversion = models.IntegerField()
