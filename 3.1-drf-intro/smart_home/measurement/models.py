from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)


class Measurement(models.Model):
    id_sensor = models.IntegerField(primary_key=True)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(max_length=50, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)