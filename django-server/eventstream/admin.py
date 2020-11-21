from django.contrib import admin
from eventstream import models
from django.contrib.admin import register


@register(models.Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ("id", "event_type", "payload", "created")
    list_display = [
        "id",
        "event_type",
        "payload",
        "created",
    ]
    list_filter = [
        "event_type",
    ]