from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('generate_data.urls')),
    path("admin/", admin.site.urls),
]
