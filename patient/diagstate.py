from django.db import models

class DiagState(models.Model):
    number = models.IntegerField(primary_key=True) #고유번호
    state = models.IntegerField(choices=[(0, '진료 대기'), (1, '진료 중')])  # 0: 진료 대기, 1: 진료 중


