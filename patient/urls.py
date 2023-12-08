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
    path('<str:patient_id>/<str:part>/<str:type>/<str:exercise>/', views.exercise_form, name='exercise_form'),
    path('<str:patient_id>/rom/', views.rom, name='rom'),
    path('<str:patient_id>/<str:part>/rom', views.rom_form, name='rom_form'),
    path('<str:patient_id>/data1/', views.data1, name='data1'),
    path('<str:patient_id>/data_index/', views.data_index, name='data_index'),
    path('<str:patient_id>/<str:part>/<str:type>/exercise_data', views.exercise_data, name='exercise_data'),
]