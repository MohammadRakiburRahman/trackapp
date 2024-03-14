
# models.py

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    # Add more fields as needed

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # Add more fields as needed

class Device(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # Add more fields as needed

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField()
    check_in_time = models.DateTimeField(blank=True, null=True)
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_checkin = models.CharField(max_length=100, blank=True, null=True)
    # Add more fields as needed

