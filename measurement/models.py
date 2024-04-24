from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name="sensor")