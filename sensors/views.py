# Create your views here.
import json
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sensors.models import DeviceGeneral, DeviceTrafficPattern, Exploit, ExploitInfo
from sensors.serializer import DeviceSerializer, DeviceTrafficPatternSerializer, DeviceExploitSerializer, DeviceExploitInofoSerializer

@api_view(['GET','POST'])
def Sensor_list(request):
    if request.method=="GET":
        sensors = DeviceGeneral.objects.all()
        sensors1 = DeviceTrafficPattern.objects.all()
        sensors2 = Exploit.objects.all()
        sensors3 = ExploitInfo.objects.all()
        serializer = DeviceSerializer(sensors,many=True)
        serializer1 = DeviceTrafficPatternSerializer(sensors1,many=True)
        serializer2 = DeviceExploitSerializer(sensors2, many = True)
        serializer3 = DeviceExploitInfoSerializer(sensors3, many = True)
        return Response({'DeviceGeneral':serializer.data, 'DeviceTrafficPattern':serializer1.data,\
                         'DeviceExploit':serializer2.data, 'DeviceExploitInfo':serializer3.data})
    elif request.method == 'POST':
        print request.body
        serializer = DeviceSerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Sensor_detail(request,pk):
    try:
        sensors = DeviceGeneral.objects.get(pk=pk)
        sensors1 = DeviceTrafficPattern.objects.get(pk=pk)
        sensors2 = Exploit.objects.filter(DeviceID=pk)
        
        sensors3 = ExploitInfo.objects.filter(DeviceID=pk)
    except DeviceGeneral.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DeviceSerializer(sensors)
        serializer1 = DeviceExploitSerializer(sensors1, many = True)
        return Response({'General':serializer.data, 'Exploit':serializer1.data})

    elif request.method == "PUT":
        serializer = DeviceGeneralSerializer(sensors,data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        sensors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
