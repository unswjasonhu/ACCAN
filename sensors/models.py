from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DeviceGeneral(models.Model):
    DeviceID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Industry = models.CharField(max_length=30)
    ReleaseDate = models.DateField()
    Description = models.TextField()
    Manufacturer = models.TextField()
    PictureUrl = models.URLField()
    Availabilty models.CharField(max_length=30)
    Price = models.IntegerField()
    Interactivity = models.TextField()
    AppName = models.TextField()
    FirmVersion = models.TextField()
    DateTested = models.DateField()
    OS = models.TextField()
    ComunicationMethod = models.TextField()
    
    
class DeviceTrafficPattern(models.Model):
    DeviceID = models.IntegerField(primary_key=True)
    SleepTime = models.IntegerField()
    ActiveVolume = models.IntegerField()
    AvgPacketSize = models.IntegerField()
    MeanRate = models.IntegerField()
    PeakRate = models.IntegerField()
    ActiveTime = models.IntegerField()
    NumServersComm = models.IntegerField()
    NumProtocols = models.IntegerField()
    UniqueDNSReq = models.IntegerField()
    DNSInterval = models.IntegerField()
    NTPInterval = models.IntegerField()
    PortsOpen = models.TextField()
    PortComm = models.TextField()
    EncryptionProtocol = models.TextField()
    
class Exploit(models.Model):
    ExploitID = models.IntegerField(primary_key=True)
    DeviceID = models.IntegerField()
    ExploitInfoID = models.IntegerField()
    ExploitDetail = models.TextField()
    Script = models.TextField()
    SamplePCAP = models.TextField()
    Characteristic = models.TextField()

class ExploitInfo(models.Model):
    ExploitInfoID = models.IntegerField(primary_key=True)
    ExploitName = models.TextField()
    ExploitInfo = models.TextField()
    
    
    
    

    

