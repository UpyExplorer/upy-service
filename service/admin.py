# coding=utf-8

"""
Module Admin
"""


from django.contrib import admin
from app.utils import get_field_list

from service.models import WorkStation

class WorkStationAdmin(admin.ModelAdmin):
    list_display = get_field_list(WorkStation)


admin.site.register(WorkStation, WorkStationAdmin)