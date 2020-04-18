from device.models import DeviceInfo
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'List All Device'

    def add_arguments(self, parser):
        parser.add_argument('status',
                            type=str,
                            nargs='?',
                            default='NA'
                            )

    def handle(self, *args, **kwargs):
        status = kwargs.get('status')
        if status in ['0', '1']:
            devices = DeviceInfo.objects.filter(status=status)
            if devices:
                return self.list_devices(devices)
            return 'Search query not presented'

        devices = DeviceInfo.objects.all()
        if devices:
            return self.list_devices(devices)
        return 'No device details are present at this moment.'

    def list_devices(self, devices):
        for device in devices:
            print('Device - {}, Status - {}'.format(device.name, device.status))
