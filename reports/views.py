from django.shortcuts import render
from rest_framework.views import APIView
from reports.models import *
from main.models import *
from reports.serializers import *
from rest_framework.response import Response
from django.db.models import F
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class DataSourceListView(APIView):
    def get(self,request):
        data = DataSource.objects.all()
        serializer = DataSourceListSerializer(data, many = True)
        return Response(serializer.data)
        

class ReportIncidentListView(APIView):
    
    def get(self,request):
        params = request.query_params
        search_field = params.get("search")
        # Base queryset
        queryset = ReportIncident.objects.all()

        # Annotate the queryset to replicate `actual_field_name` logic
        queryset = queryset.annotate(
            actual_field_name=F('field_name')  # Replicating the logic here if needed
        )

        # Apply filtering based on the annotated field
        if search_field:
            queryset = queryset.filter(actual_field_name__icontains=search_field)

        serializer = ReportIncidentListSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ReportIncidentTableView(APIView):
    pagination_class = PageNumberPagination
    
    def post(self,request):
        data = request.data
        fields = data.get("fields")
        
        not_exist = [field for field in fields if field not in [f.name for f in Incident._meta.get_fields()]]
        if len(not_exist) > 0:
            raise serializers.ValidationError(f"Invalid fields {not_exist}")
        
        queryset = Incident.objects.all()
        
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        if paginated_queryset is not None:
            # Serialize the paginated data
            serializer = ReportIncidentTableSerializer(paginated_queryset, fields=fields, many=True)
            pagination_data =  paginator.get_paginated_response(serializer.data)
            f_fields = format_field_name(fields)
        
            response_data = {}
            response_data.update(pagination_data.data)
            response_data['labels'] = f_fields
               
            return Response(response_data)
        # # If no pagination is applied, serialize the entire queryset
        # serializer = ReportIncidentTableSerializer(queryset, fields=fields, many=True)
        # return Response(serializer.data)

        