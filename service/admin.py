# coding=utf-8

"""
Module Admin
"""


from django.contrib import admin
from app.utils import get_field_list

from service.models import (
    WorkStation,
    WorkUser,
    WorkProcess
    )

class WorkStationAdmin(admin.ModelAdmin):
    list_display = get_field_list(WorkStation)

    
class WorkUSerAdmin(admin.ModelAdmin):
    list_display = get_field_list(WorkUser)


class WorkProcessAdmin(admin.ModelAdmin):
    list_display = get_field_list(WorkProcess)

    
admin.site.register(WorkStation, WorkStationAdmin)
admin.site.register(WorkUser, WorkUSerAdmin)
admin.site.register(WorkProcess, WorkProcessAdmin)