from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DeviceGeneral(models.Model):
    DeviceID=models.IntegerField(max_length=30, primary_key=True)
    SleepTime
    ActiveVolume 
    AvgPacketSize
    Mean Rate 
    

    

