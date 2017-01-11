from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DeviceGeneral(models.Model):
    DeviceID = models.IntegerField(primary_key=True)
    Name = models.TextField()
    Category = models.TextField()
    Industry = models.TextField()
    ReleaseDate = models.DateField()
    Description = models.TextField()
    Manufacturer = models.TextField()
    PictureUrl = models.URLField()
    Availabilty = models.CharField(max_length=30)
    Price = models.IntegerField()
    Interactivity = models.TextField()
    AppName = models.TextField()
    FirmVersion = models.TextField()
    DateTested = models.DateField()
    OS = models.TextField()
    ComunicationMethod = models.TextField()
    def __str__(self):
        return u'%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.DeviceID, self.Name, self.Category, self.Industry, self.ReleaseDate, self.Description, self.Manufacturer, self.PictureUrl, self.Availabilty, self.Price
                                                Interactivity = models.TextField()
                                                    AppName = models.TextField()
                                                        FirmVersion = models.TextField()
                                                            DateTested = models.DateField()
                                                                OS = models.TextField()
                                                                    ComunicationMethod = models.TextField())
    
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
    def __str__(self):
        return u'%s' % (self.DeviceID) 
    
class Exploit(models.Model):
    ExploitID = models.IntegerField(primary_key=True)
    DeviceID = models.IntegerField()
    ExploitInfoID = models.IntegerField()
    ExploitDetail = models.TextField()
    Script = models.TextField()
    SamplePCAP = models.TextField()
    Characteristic = models.TextField()
    def __str__(self):
        return u'%s' % (self.ExploitID) 
    
class ExploitInfo(models.Model):
    ExploitInfoID = models.IntegerField(primary_key=True)
    ExploitName = models.TextField()
    ExploitInfo = models.TextField()
    def __str__(self):
        return u'%s' % (self.ExploitInfoID)     
    
    
    

    

