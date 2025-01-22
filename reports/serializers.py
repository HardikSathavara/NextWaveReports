from rest_framework import serializers
from main.models import *
from reports.models import *

class DataSourceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = "__all__"
        

class ReportIncidentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportIncident
        fields = "__all__"
    
    
class ReportIncidentTableSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)  # Extract `fields` parameter
        super().__init__(*args, **kwargs)  # Initialize the serializer
        
        self.Meta.fields = fields
    
    class Meta:
        model = Incident
        fields = []
        
{
"fields":["uuid","id"]
}