from django.contrib.postgres.fields import JSONField
from django.db import models


class Event(models.Model):
    type = models.CharField(max_length=255)
    payload = JSONField()
    created = models.DateTimeField(auto_now_add=True)
