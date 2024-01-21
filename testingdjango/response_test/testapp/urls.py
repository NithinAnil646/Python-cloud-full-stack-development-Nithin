# testapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('normal_response/', normal_response),
    path('redirect_response/', redirect_response),
    path('permanent_redirect_response/', permanent_redirect_response),
    path('not_modified_response/', not_modified_response),
    path('bad_request_response/', bad_request_response),
    path('forbidden_response/', forbidden_response),
    path('not_allowed_response/', not_allowed_response),
    path('gone_response/', gone_response),
    path('server_error_response/', server_error_response),
    path('not_found_response/', not_found_response),
    path('json_response/', json_response),
    path('streaming_response/', streaming_response),
    path('file_response/', file_response),
]
