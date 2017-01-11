from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DeviceGeneral, DeviceTrafficPattern, Exploit, ExploitInfo

admin.site.register(DeviceGeneral)
admin.site.register(DeviceTrafficPattern)
admin.site.register(Exploit)
admin.site.register(ExploitInfo)
