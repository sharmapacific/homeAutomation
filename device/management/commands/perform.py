from device.models import DeviceInfo
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Perform Action on Device'

    def add_arguments(self, parser):
        parser.add_argument('device',
                            type=str,
                            help='Indicates the device'
                            )
        parser.add_argument('status',
                            type=str
                            )

    def handle(self, *args, **kwargs):
        device = kwargs.get('device')
        status = kwargs.get('status')
        if self.check_exists(device):
            DeviceInfo.objects.filter(name=device).update(status=status)
            return 'Action has been Performed'
        return 'No Such device exists, Please add it first'

    def check_exists(self, device):
        if DeviceInfo.objects.filter(name=device).exists():
            return True
