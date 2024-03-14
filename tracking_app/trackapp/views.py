# assets_tracking/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company, Employee, Device, DeviceLog
from .forms import CompanyForm, EmployeeForm, DeviceForm, DeviceLogForm

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices': devices})

def device_log_list(request):
    device_logs = DeviceLog.objects.all()
    return render(request, 'device_log_list.html', {'device_logs': device_logs})

@login_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company added successfully!')
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'add_company.html', {'form': form})

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

@login_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device added successfully!')
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'add_device.html', {'form': form})

@login_required
def add_device_log(request):
    if request.method == 'POST':
        form = DeviceLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device log added successfully!')
            return redirect('device_log_list')
    else:
        form = DeviceLogForm()
    return render(request, 'add_device_log.html', {'form': form})
