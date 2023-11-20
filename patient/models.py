from django.db import models

# Create your models here.
class Patient(models.Model):
    number = models.IntegerField(primary_key=True) #고유번호
    name = models.CharField(max_length=10) # 이름
    front_resident = models.CharField(max_length=10) # 앞 주민번호
    back_resident = models.CharField(max_length=10) # 뒤 주민번호
    phone = models.CharField(max_length=30) 