# cloudms/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('msgapp/', include('msgapp.urls')),
]
