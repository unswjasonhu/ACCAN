
fromrest_frameworkimportserializers

from sensors.models import DeviceGeneral


class DeviceSerializer(serializers.ModelSerializer):
    classMeta:
        model=DeivceGeneral
        fields=("DeviceID","Name","Category","Industry",\
        "ReleaseDate","Description","Manufacturer",\
        "PictureUrl","Availabilty","Price",\
        "Interactivity","AppName","FirmVersion",\
        "DateTested","OS","ComunicationMethod")
