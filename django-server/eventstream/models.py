import uuid

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone


class Event(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4)
    event_type = models.CharField(max_length=64)
    payload = JSONField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} - {self.event_type}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            frontend_event_payload = {
                "activityType": self.event_type,
                "data": self.payload,
                "timestamp": self.created.timestamp(),
            }
            settings.NOTIFICATION_SERVICE.publish_notification(
                "eventstream", frontend_event_payload
            )
        except NotImplementedError:
            pass
