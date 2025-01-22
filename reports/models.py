from django.db import models
from reports.custom_utils.utils import *
from reports.custom_utils.enums import *

# Create your models here.

class DataSource(models.Model):
    data_source_name = models.CharField(max_length=128, null=False, blank=False)
    
    @property
    def model_instance(self):
        return DataSourceEnum[self.data_source_name].value
        
    def __str__(self):
        return self.data_source_name
    
    

class ReportIncident(models.Model):
    field_name = models.CharField(max_length=128, null=False, blank=False)
    edited_field_value = models.CharField(max_length=1028, null=True, blank=True)
    
    @property
    def actual_field_name(self):
        f_field = format_field_name([self.field_name])
        return f_field[0][self.field_name]
    
    @actual_field_name.setter
    def actual_field_name(self, value):
        self.field_name = value  # Update the underlying field

    def save(self, *args, **kwargs):
        if not self.edited_field_value:
            self.edited_field_value = self.actual_field_name
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.field_name
        

class ReportDataSourceSelectedField(models.Model):
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, null=False, blank=False)
    selected_fields = models.ManyToManyField(ReportIncident)
    
    def __str__(self):
        return self.data_source.data_source_name
    
    
class Report(models.Model):
    report_name = models.CharField(max_length=128, null=False, blank=False)
    data_source_selected_fields = models.ManyToManyField(ReportDataSourceSelectedField)
    # selected_fields = models.ManyToManyField(ReportIncident)
    
    def __str__(self):
        return self.report_name
    
    
    # {
    #     "report_name":"Report 1",
    #     "data_sources": [
    #         {
                
    #             "data_source_name":"Incident",
    #             "results":[
    #                 {
    #                     "id":44,
    #                     "created_at": 1
    #                 },
    #                 {
    #                     "id":45,
    #                     "created_at": 2
    #                 }
    #             ],
    #             "labels":{
    #                 "id": "Id",
    #                 "created_at": "Created At"
    #             },
    #             "selected_fields":[
    #                 {
    #                     "id":"Id",
    #                     "created_at": "Created At"
    #                 }
    #             ]
    #         },
    #         {
    #             "data_source_name":"Daily Log",
    #             "results":[
    #                 {
    #                     "id":56565,
    #                     "status": 1
    #                 },
    #                 {
    #                     "id":2323,
    #                     "status": 2
    #                 }
    #             ],
    #             "labels":{
    #                 "id": "Id",
    #                 "status": "Status"
    #             },
    #             "selected_fields":[
    #                 {
    #                     "id":"Id",
    #                     "status": "Status of User"
    #                 }
    #             ]
    #         }
    #     ]
    # }