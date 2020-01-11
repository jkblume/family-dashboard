import logging

from django.conf import settings
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from actions.builder import PayloadBuilder
from actions.models import AppPerson
from eventstream.models import Event

logger = logging.getLogger(__name__)


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
def detected_person(request: Request) -> Response:
    person_id = request.data.get("personId")
    person_image = request.data.get("personImage")

    app_person = AppPerson.objects.filter(
        app=AppPerson.App.DETECT_FACE, app_specific_id=person_id
    ).first()

    person = None
    if app_person is not None:
        person = app_person.person

    event_payload = PayloadBuilder.build_detected_person_payload(person, person_image)
    Event.objects.create(
        event_type=Event.EventType.DETECTED_FACE, payload=event_payload
    )

    return Response(status=200)


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
def strava_activity(request: Request) -> Response:
    logger.info(request.data)
    strava_webhook_event_data = request.data

    # check data for being a "created activity event"
    if strava_webhook_event_data.get("aspect_type") != "create":
        return Response(status=200)

    strave_athlete_id = str(strava_webhook_event_data.get("owner_id"))
    app_person = AppPerson.objects.filter(
        app=AppPerson.App.STRAVA, app_specific_id=strave_athlete_id
    ).first()

    person = None
    if app_person is not None:
        person = app_person.person

    event_payload = PayloadBuilder.build_strava_activity_payload(person)
    Event.objects.create(
        event_type=Event.EventType.STRAVA_ACTIVITY, payload=event_payload
    )

    return Response(status=200)
