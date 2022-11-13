from django.contrib import admin
from django.urls import path, include

from edi_employee_management.settings import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("employee/", include("employee.urls")),
    path("work/", include("work.urls")),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
]
