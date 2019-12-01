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
    person_id = request.data.get("personId")
    print(person_id)
    person_image = request.data.get("personImage")
    person = Person.objects.filter(id=person_id).first()
    
    event_payload = PayloadBuilder.build_detected_person_payload(person, person_image)
    Event.objects.create(type="detected_person", payload=event_payload)

    return Response(status=200)
