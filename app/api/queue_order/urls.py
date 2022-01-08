# coding=utf-8

"""
Module Docstring
"""

from django.urls import path
from app.api.queue_order.views import queue_order

urlpatterns = [
    path('', queue_order)
]
