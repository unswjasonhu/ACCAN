
from rest_framework import serializers

from .models import DeviceGeneral


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeviceGeneral
        fields=("DeviceID","Name","Category","Industry",\
        "ReleaseDate","Description","Manufacturer",\
        "PictureUrl","Availabilty","Price",\
        "Interactivity","AppName","FirmVersion",\
        "DateTested","OS","ComunicationMethod")
