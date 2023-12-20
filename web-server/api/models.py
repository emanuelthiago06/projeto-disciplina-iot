from django.db import models

# Create your models here.

class Sensor(models.Model):
    id_personal = models.IntegerField(null=True)
    value = models.FloatField()
    created_at = models.DateField(null=True)