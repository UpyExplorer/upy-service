# coding=utf-8

"""
Source App
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('backoffice/', admin.site.urls),
]
