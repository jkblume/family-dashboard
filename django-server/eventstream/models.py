from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone


class Event(models.Model):
    type = models.CharField(max_length=255)
    payload = JSONField()
    created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            settings.NOTIFICATION_SERVICE.publish_notification(self.payload)
        except NotImplementedError:
            pass
