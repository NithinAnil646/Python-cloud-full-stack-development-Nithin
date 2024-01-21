# response_test/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('response_test/testapp/', include('testapp.urls')),
]
