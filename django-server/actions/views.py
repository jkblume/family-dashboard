import logging
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from actions.builder import PayloadBuilder
from actions.models import Person
from eventstream.models import Event

logger = logging.getLogger(__name__)


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
def detected_person(request: Request) -> Response:
    person_id = request.data.get("person_id")
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        logger.error(f"can't find person for id {person_id}")
        return Response(
            status=404,
            data={
                "error": {
                    "message": f"can't find person for id {person_id}",
                    "code": "404",
                }
            },
        )

    event_payload = PayloadBuilder.build_detected_person_payload(person)
    Event.objects.create(type="detected_person", payload=event_payload)

    return Response(status=200)
