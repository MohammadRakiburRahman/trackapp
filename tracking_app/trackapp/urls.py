#urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('devices/', views.device_list, name='device_list'),
    path('device-logs/', views.device_log_list, name='device_log_list'),
    path('add-company/', views.add_company, name='add_company'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('add-device/', views.add_device, name='add_device'),
    path('add-device-log/', views.add_device_log, name='add_device_log'),
]

