from django.shortcuts import render

# Create your views here.
from eventstream.models import Event, Activity


def get_eventstream(request):
    actvities = Activity.objects.filter(duration__gt=3)