# coding=utf-8

"""
Module Docstring
"""

from django.urls import path
from app.api.queue_ads.views import queue_ads

urlpatterns = [
    path('', queue_ads)
]
