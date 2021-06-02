from django.db import models


class Reflectance(models.Model):
    sensor_value1 = models.IntegerField()
    sensor_value2 = models.IntegerField()
    sensor_value3 = models.IntegerField()
    sensor_value4 = models.IntegerField()
    sensor_value5 = models.IntegerField()
    sensor_value6 = models.IntegerField()
    sensor_value7 = models.IntegerField()
    timeStamp = models.TimeField(auto_now_add=True)

class Distance(models.Model):
    sensor_number = models.IntegerField()
    distance_value = models.IntegerField()
    timeStamp = models.TimeField(auto_now_add=True)
    
