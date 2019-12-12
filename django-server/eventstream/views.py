from eventstream.builder import ResponseDataBuilder


@api_view(["GET"])
@renderer_classes((JSONRenderer,))
def get_events(request: Request) -> Response:
    result = []
    last_n_events = request.queryparam()

    # get last k events out of database and pass it back

    return Response(data=ResponseDataBuilder.build_success_response(result), status=200)
