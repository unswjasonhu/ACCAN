csv_filepath="/home/ke/mysite/rawdata/"
# Full path to your django project directory
your_djangoproject_home="/home/ke/mysite/"
    
import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()
from sensors.models import DeviceGeneral, DeviceTrafficPattern, Exploit, ExploitInfo
import csv
dataReader1 = csv.reader(open(csv_filepath+ 'DeviceGeneral.tsv'), dialect='excel-tab')
dataReader2 = csv.reader(open(csv_filepath+ 'DeviceTrafficPattern.tsv'), dialect='excel-tab')
dataReader3 = csv.reader(open(csv_filepath+ 'Exploit.tsv'), dialect='excel-tab')
dataReader4 = csv.reader(open(csv_filepath+ 'ExploitInfo.tsv'), dialect='excel-tab')

for row in dataReader1:
    if row[0] != 'DeviceID': # Ignore the header row, import everything else
        sensors1 = DeviceGeneral()
        sensors1.DeviceID = row[0]
        sensors1.Name = row[1]
        sensors1.Category = row[2]
        sensors1.Industry = row[3]
        sensors1.ReleaseDate = row[4]
        sensors1.Description = row[5]
        sensors1.Manufacturer = row[6]
        sensors1.PictureUrl = row[7]
        sensors1.Availabilty = row[8]
        sensors1.Price = row[9]
        sensors1.Interactivity = row[10]
        sensors1.AppName = row[11]
        sensors1.FirmVersion = row[12]
        sensors1.DateTested = row[13]
        sensors1.OS = row[14]
        sensors1.ComunicationMethod = row[15]
        print sensors1
        sensors1.save()

for row in dataReader2:
    if row[0]!= 'DeviceID':
        sensor2 = DeviceTrafficPattern()
        sensor2.DeviceID = row[0]
        sensor2.SleepTime = row[1]
        sensor2.ActiveVolume = row[2]
        sensor2.AvgPacketSize = row[3]
        sensor2.MeanRate = row[4]
        sensor2.PeakRate = row[5]
        sensor2.ActiveTime = row[6]
        sensor2.NumServersComm = row[7]
        sensor2.NumProtocols = row[8]
        sensor2.UniqueDNSReq = row[9]
        sensor2.DNSInterval = row[10]
        sensor2.NTPInterval = row[11]
        sensor2.PortsOpen = row[12]
        sensor2.PortComm = row[13]
        sensor2.EncryptionProtocol = row[14]
        print sensor2
        sensor2.save()
