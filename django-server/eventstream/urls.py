from django.urls import path

from eventstream import views

urlpatterns = [path("events", views.get_events)]
