# coding=utf-8

"""
Module Admin
"""


from django.contrib import admin
from app.utils import get_field_list

from service.models import WorkStation, WorkUser

class WorkStationAdmin(admin.ModelAdmin):
    list_display = get_field_list(WorkStation)
    
class WorkUSerAdmin(admin.ModelAdmin):
    list_display = get_field_list(WorkUser)


admin.site.register(WorkStation, WorkStationAdmin)
admin.site.register(WorkUser, WorkUSerAdmin)