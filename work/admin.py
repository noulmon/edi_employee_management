from django.contrib import admin

from .models import WorkArrangement, EmployeeWorkArrangement

# Register your models here.
admin.site.register(WorkArrangement)
admin.site.register(EmployeeWorkArrangement)
