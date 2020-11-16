from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from django.conf import settings

from eventstream.builders import ResponseDataBuilder
from eventstream.models import Event


@api_view(["GET"])
@renderer_classes((JSONRenderer,))
def get_events(request: Request) -> Response:
    return Response(data=ResponseDataBuilder.build_success_response([]), status=200)


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
def post_event(request: Request) -> Response:
    event_payload = request.data.get("eventPayload")
    event_type = request.data.get("eventType")
    event = Event.objects.create(event_type=event_type, payload=event_payload)

    return Response(
        data=ResponseDataBuilder.build_success_response({"id": str(event.id)}),
        status=200,
    )


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
def full_size_detail(request: Request) -> Response:
    try:
        settings.NOTIFICATION_SERVICE.publish_notification(
            "controls", {"control": "full_size_detail", "data": {"time": 10}}
        )
    except NotImplementedError:
        pass

    return Response(data=ResponseDataBuilder.build_success_response({}), status=200,)
