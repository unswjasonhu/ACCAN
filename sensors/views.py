# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from sensors.models import DeviceGeneral

def search_form(request):
        return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        devicegeneral = DeviceGeneral.objects.filter(Name__icontains=q)
        return render(request, 'search_results.html',\
                {'devicegeneral': devicegeneral, 'query': q})
    else:
        return render(request, 'search_form.html', {'error': True})
