import uuid
from django.db import models


class Person(models.Model):
    id = models.CharField(max_length=255, default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AppPerson(models.Model):
    class Meta:
        unique_together = ("app", "app_specific_id")

    class App(models.TextChoices):
        STRAVA = "STRAVA"
        DETECT_FACE = "DETECT_FACE"

    person = models.ForeignKey("Person", on_delete=models.PROTECT)
    app = models.CharField(max_length=64, choices=App.choices)
    app_specific_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.person.id} with app {self.app} id {self.app_specific_id}"
