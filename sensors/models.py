from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DeviceGeneral(models.Model):
    DeviceID = models.IntegerField(max_length=30, primary_key=True)
    SleepTime = models.IntegerField(max_length=30)
    ActiveVolume = models.IntegerField(max_length=30)
    AvgPacketSize = models.IntegerField(max_length=30)
    MeanRate = models.IntegerField(max_length=30)
    PeakRate = models.IntegerField(max_length=30)
    ActiveTime = models.IntegerField(max_length=30)
    NumServersComm = models.IntegerField(max_length=30)
    NumProtocols = models.IntegerField(max_length=30)
    UniqueDNSReq = models.IntegerField(max_length=30)
    DNSInterval = models.IntegerField(max_length=30)
    NTPInterval = models.IntegerField(max_length=30)
    PortsOpen = models.TextField()
    PortComm = models.TextField()
    EncryptionProtocol = models.TextField()
    
    
    
    

    

