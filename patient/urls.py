from django.urls import path, include
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.patient_add, name='patient_add'),
    path('<str:patient_id>/detail/', views.detail, name='detail'),
    path('<str:patient_id>/exercise/', views.exercise, name='exercise'),
]