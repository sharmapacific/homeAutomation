import uuid

from django.db import models


class DeviceInfo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    name = models.CharField(max_length=500, db_index=True, blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created At',
                                      db_index=True)

    def __str__(self):
        return '%s ' % (self.name)
