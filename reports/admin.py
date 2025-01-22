from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ['id','data_source_name']


@admin.register(ReportIncident)
class ReportIncidentAdmin(admin.ModelAdmin):
    list_display = ['id','field_name', 'edited_field_value', 'actual_field_name']
    

@admin.register(ReportDataSourceSelectedField)
class ReportDataSourceSelectedFieldAdmin(admin.ModelAdmin):
    list_display = ['id','data_source']
    

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id','report_name']