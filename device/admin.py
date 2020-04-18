from device.models import DeviceInfo

from django.contrib import admin


@admin.register(DeviceInfo)
class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at',)
    search_fields = ('name', 'status', 'created_at',)
