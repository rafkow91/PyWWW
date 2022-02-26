from django.contrib import admin

from .models import BloodPressureMeasurement

@admin.register(BloodPressureMeasurement)
class BloodpressuresAdmin(admin.ModelAdmin):
    pass
