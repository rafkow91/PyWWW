from django.contrib import admin

from .models import GlucoseMeasurement

@admin.register(GlucoseMeasurement)
class GlucosesAdmin(admin.ModelAdmin):
    pass
