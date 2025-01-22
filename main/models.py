from django.db import models

# Create your models here.


class Incident(models.Model):
    incident_name = models.CharField(max_length=128, null=False, blank=False, unique= True)
    uuid = models.CharField(max_length=1028, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.incident_name