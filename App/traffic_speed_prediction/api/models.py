from django.contrib.postgres.fields import ArrayField
from django.db import models


class WeatherHistoryData(models.Model):
    roadStationId = models.IntegerField(default=0, unique=False)
    sensorId = models.IntegerField(default=0, unique=False)
    sensorValue = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, unique=False)
    measuredTime = models.CharField(max_length=20, default="", unique=False)

class Road(models.Model):
    Road_number = models.IntegerField()


class Road_section(models.Model):
    road_section_number = models.IntegerField()
    road = models.ForeignKey('Road', on_delete=models.CASCADE)
    roadTemperature = models.TextField()
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    daylight = models.BooleanField()
    weatherSymbol = models.TextField()
    roadMaintenanceClass = models.TextField()
    freeFlowSpeed1 = models.TextField()
    average_speed = models.FloatField(default=0)
    roadName = models.TextField(default="")


class TMS_station(models.Model):
    tms_station = models.IntegerField()
    roadSection = models.ForeignKey('Road_section', on_delete=models.CASCADE)



class PredictionResponse(models.Model):
    roadId = models.IntegerField(default=0)
    roadName = models.TextField(default="")
    roadSectionId = models.IntegerField(default=0)
    predictedSpeed = models.FloatField(default=0)
    selectedRoads = models.TextField(default="")