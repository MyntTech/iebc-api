from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Diaspora(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    area_code = models.CharField(max_length=200)
    area_name = models.CharField(max_length=200)
    center = models.CharField(max_length=200)
    center_code = models.CharField(max_length=200)
    polling_station_code = models.CharField(max_length=200)
    polling_station_name = models.CharField(max_length=200)
    voters = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name