from django.urls import path, include
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.patient_add, name='patient_add'),
    path('<str:patient_id>/detail/', views.detail, name='detail'),
    path('<str:patient_id>/modify', views.patient_modify, name = 'patient_modify'),
    path('<str:patient_id>/exercise/', views.exercise, name='exercise'),
    path('<str:patient_id>/<str:part>/<str:type>/', views.exercise_add, name='exercise_add'),
    path('<str:patient_id>/rom/', views.rom, name='rom'),
    
]