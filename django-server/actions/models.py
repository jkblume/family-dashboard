import uuid

from django.db import models


class Person(models.Model):
    id = models.CharField(max_length=255, default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
