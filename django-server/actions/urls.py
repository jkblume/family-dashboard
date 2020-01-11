from django.urls import path

from actions import views

urlpatterns = [
    path("detected_person", views.detected_person),
    path("strava_activity", views.strava_activity),
]
