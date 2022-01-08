# coding=utf-8

"""
Source App
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('backoffice/', admin.site.urls),
    path('api/', include('app.api.urls'))
]
