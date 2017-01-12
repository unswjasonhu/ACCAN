
from rest_framework import serializers

from .models import DeviceGeneral, DeviceTrafficPattern, Exploit


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeviceGeneral
        fields=("DeviceID","Name","Category","Industry",\
        "ReleaseDate","Description","Manufacturer",\
        "PictureUrl","Availabilty","Price",\
        "Interactivity","AppName","FirmVersion",\
        "DateTested","OS","ComunicationMethod")

class DeviceTrafficePatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exploit
        fields= ("ExploitID", "DeviceID", "ExploitInfoID", "ExploitDetail",\
                "Script", "SamplePCAP", "Characteristic")
        
        
class DeviceExploitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exploit
        fields= ("ExploitID", "DeviceID", "ExploitInfoID", "ExploitDetail",\
                "Script", "SamplePCAP", "Characteristic")

