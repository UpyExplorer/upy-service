# coding=utf-8

"""
Module Docstring
"""

from django.urls import path, include
from app.api.views import hello_world

urlpatterns = [
    path('hello_world/', hello_world)
]
