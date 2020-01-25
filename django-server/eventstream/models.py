from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone


class Event(models.Model):
    class EventType(models.TextChoices):
        STRAVA_ACTIVITY = "STRAVA_ACTIVITY"
        DETECTED_FACE = "DETECTED_FACE"

    event_type = models.CharField(max_length=64, choices=EventType.choices)
    payload = JSONField(null=True, blank=True)
    frontend_payload = JSONField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} - {self.event_type}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            settings.NOTIFICATION_SERVICE.publish_notification(self.frontend_payload)
        except NotImplementedError:
            pass
