import logging

from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from actions.builders import PayloadBuilder
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

    event_frontend_payload = PayloadBuilder.build_detected_person_frontend_payload(
        person, person_image
    )
    Event.objects.create(
        event_type=Event.EventType.DETECTED_FACE,
        frontend_payload=event_frontend_payload,
    )

    return Response(status=200)
