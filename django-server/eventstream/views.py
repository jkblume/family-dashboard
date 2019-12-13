from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from eventstream.builder import ResponseDataBuilder


@api_view(["GET"])
@renderer_classes((JSONRenderer,))
def get_events(request: Request) -> Response:
    result = []
    last_n_events = request.queryparam()

    # get last k events out of database and pass it back

    return Response(data=ResponseDataBuilder.build_success_response(result), status=200)
