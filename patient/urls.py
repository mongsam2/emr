from django.urls import path, include
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.patient_add, name='patient_add'),
    path('<str:patient_id>/detail/', views.detail, name='detail'),
    path('<str:patient_id>/modify/', views.patient_modify, name = 'patient_modify'),
    path('<str:patient_id>/<str:selected_date>/exercise/', views.exercise, name='exercise'),
    path('<str:patient_id>/<str:part>/<str:type>/<str:selected_date>/add/', views.exercise_add, name='exercise_add'),
    path('<str:patient_id>/<str:part>/<str:type>/<str:exercise>/<str:selected_date>/form/', views.exercise_form, name='exercise_form'),
    path('<str:patient_id>/<str:exercise_code>/<str:selected_date>/modify/', views.exercise_modify, name='exercise_modify'),
    path('<str:patient_id>/rom/', views.rom, name='rom'),
    path('<str:patient_id>/<str:part>/rom', views.rom_form, name='rom_form'),
    path('<str:patient_id>/data1/', views.data1, name='data1'),
    path('<str:patient_id>/data2/', views.data2, name='data2'),
    path('<str:patient_id>/data_index/', views.data_index, name='data_index'),
    path('<str:patient_id>/<str:part>/<str:type>/exercise/data/', views.exercise_data, name='exercise_data'),
    path('<str:patient_id>/<str:part>/<str:type>/<str:exercise>/exercise_graph', views.exercise_graph, name='exercise_graph'),
    path('<str:patient_id>/<str:part>/rom_graph', views.rom_graph, name = 'rom_graph')
]