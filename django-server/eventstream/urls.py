from django.urls import path

from eventstream import views

urlpatterns = [
    path("events/", views.get_events),
    path("events/post_event/", views.post_event),
    path("controlls/full_size_detail/", views.full_size_detail_control),
]
