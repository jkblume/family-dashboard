from django.contrib import admin
from eventstream.models import Event, Activity

admin.site.register(Event)
admin.site.register(Activity)
