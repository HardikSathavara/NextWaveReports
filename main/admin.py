from django.contrib import admin
from main.models import *

# Register your models here.

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['id','incident_name','uuid']