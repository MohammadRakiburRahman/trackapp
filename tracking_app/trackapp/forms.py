# assets_tracking/forms.py

from django import forms
from .models import Company, Employee, Device, DeviceLog

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'company']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'company']

class DeviceLogForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = ['device', 'employee', 'check_out_time', 'check_in_time', 'condition_on_checkout', 'condition_on_checkin']
