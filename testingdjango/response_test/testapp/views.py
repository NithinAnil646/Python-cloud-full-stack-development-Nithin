# testapp/views.py
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, \
    HttpResponseNotModified, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, \
    HttpResponseGone, HttpResponseServerError, HttpResponseNotFound, JsonResponse, StreamingHttpResponse, FileResponse

def normal_response(request):
    return HttpResponse("This is a normal HTTP response.")

def redirect_response(request):
    return HttpResponseRedirect('/response_test/testapp/normal_response/')

def permanent_redirect_response(request):
    return HttpResponsePermanentRedirect('/response_test/testapp/normal_response/')

def not_modified_response(request):
    return HttpResponseNotModified()

def bad_request_response(request):
    return HttpResponseBadRequest("Bad Request")

def forbidden_response(request):
    return HttpResponseForbidden("Forbidden")

def not_allowed_response(request):
    return HttpResponseNotAllowed(['GET', 'POST'], "Method Not Allowed")

def gone_response(request):
    return HttpResponseGone("Gone")

def server_error_response(request):
    return HttpResponseServerError("Internal Server Error")

def not_found_response(request):
    return HttpResponseNotFound("Page Not Found")

def json_response(request):
    data = {'message': 'This is a JSON response.'}
    return JsonResponse(data)

def streaming_response(request):
    def streaming_content():
        yield b'Part 1 of the content. '
        yield b'Part 2 of the content. '

    return StreamingHttpResponse(streaming_content(), content_type="text/plain")

def file_response(request):
    file_path = '/home/nithin/Desktop/testingdjango/response_test/testapp/templates/flower.jpeg'  # Replace with the actual file path
    return FileResponse(open(file_path, 'rb'))
