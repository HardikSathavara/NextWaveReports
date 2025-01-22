from django.urls import path
from reports.views import *


urlpatterns = [
    path("reports/data-sources", DataSourceListView.as_view()),
    path("reports/data-sources/incidents/fields", ReportIncidentListView.as_view()),
    path("reports/data-sources/incidents/table", ReportIncidentTableView.as_view()),
    
]
