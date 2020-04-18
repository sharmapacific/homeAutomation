from device.models import DeviceInfo
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete Device'

    def add_arguments(self, parser):
        parser.add_argument('device',
                            type=str,
                            nargs='?',
                            default='NA',
                            help='Indicates the device'
                            )

    def handle(self, *args, **kwargs):
        device = kwargs.get('device')
        if device == 'NA':
            DeviceInfo.objects.all().delete()
            return 'All Devices has been Deleted'

        if self.check_exists(device):
            DeviceInfo.objects.filter(name=device).delete()
            return 'Device has been Deleted'
        return 'No Such device exists, Please add it first'

    def check_exists(self, device):
        if DeviceInfo.objects.filter(name=device).exists():
            return True
