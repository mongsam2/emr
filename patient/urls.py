from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:patient_number>/', views.detail, name='detail'),
    path('patient_add/', views.patient_add, name='patient_add'),
]