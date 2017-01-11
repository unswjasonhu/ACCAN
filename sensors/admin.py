from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DeviceGeneral, DeviceTrafficPattern, Exploit, ExploitInfo

class DeviceGeneralAdmin(admin.ModelAdmin):
    list_display = ('DeviceID','Name')
    search_fields = ('Name','Category','Industry','Manufacturer')
    list_filter = ('Category',)
class DeviceTrafficPatternAdmin(admin.ModelAdmin):
    list_display = ('DeviceID','PortsOpen','PortComm')
class ExploitAdmin(admin.ModelAdmin):
    list_display = ('ExploitID','DeviceID','ExploitInfoID')
class ExploitInfoAdmin(admin.ModelAdmin):
        list_display = ('ExploitInfoID','ExploitName')

admin.site.register(DeviceGeneral, DeviceGeneralAdmin)
admin.site.register(DeviceTrafficPattern,DeviceTrafficPatternAdmin)
admin.site.register(Exploit, ExploitAdmin)
admin.site.register(ExploitInfo, ExploitInfoAdmin)
