# coding=utf-8

"""
Module Docstring
"""

from django.urls import path, include

urlpatterns = [
    path('queue_ads/', include('app.api.queue_ads.urls')),
    path('queue_product/', include('app.api.queue_product.urls'))
]
