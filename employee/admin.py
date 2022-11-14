from django.contrib import admin

from .models import Employee, Team, TeamLeader

# Register your models here.
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(TeamLeader)
