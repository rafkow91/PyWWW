from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


from main.models import Timestamped


class BloodPressureMeasurement(Timestamped):
    systolic_blood_pressure = models.PositiveSmallIntegerField()
    diastolic_blood_pressure = models.PositiveSmallIntegerField()
    measurement_datetime = models.DateTimeField(default=datetime.today)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.measurement_date} - {self.systolic_blood_pressure}/{self.diastolic_blood_pressure} mmHg'