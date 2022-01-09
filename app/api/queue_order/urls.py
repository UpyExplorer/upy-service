# coding=utf-8

"""
Module Docstring
"""

from django.urls import path
from app.api.queue_order.views import QueueOrderView

urlpatterns = [
    path('', QueueOrderView.as_view())
]
