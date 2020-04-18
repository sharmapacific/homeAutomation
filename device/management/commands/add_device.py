from device.models import DeviceInfo
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add New Device'

    def add_arguments(self, parser):
        parser.add_argument('device',
                            type=str,
                            help='Indicates the device to be add'
                            )

    def handle(self, *args, **kwargs):
        data = {
            'name': kwargs.get('device')
        }
        if self.check_duplicate(data):
            return 'The Device detail is already presented.'

        DeviceInfo.objects.create(**data)
        return 'The Device has been added.'

    def check_duplicate(self, data):
        if DeviceInfo.objects.filter(**data).exists():
            return True
