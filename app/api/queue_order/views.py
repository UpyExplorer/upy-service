# coding=utf-8

"""
Module API
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class QueueOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "queue_order"}
        return Response(content)
