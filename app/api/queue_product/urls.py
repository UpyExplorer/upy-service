# coding=utf-8

"""
Module Docstring
"""

from django.urls import path
from app.api.queue_product.views import QueueProductView

urlpatterns = [
    path('', QueueProductView.as_view())
]
