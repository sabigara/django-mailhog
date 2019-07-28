from django.contrib import admin
from django.contrib.auth import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
