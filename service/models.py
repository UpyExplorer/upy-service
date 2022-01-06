# coding=utf-8

"""
Model Config
"""

from django.db import models

class WorkStation(models.Model):
    """
    Model WorkStation
    """
    key = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    ip_address = models.CharField(max_length=15, blank=False, null=False)
    mac_address = models.CharField(max_length=50, blank=False, null=False)
    user_name = models.CharField(max_length=25, blank=False, null=False)
    host = models.CharField(max_length=25, blank=False, null=False)
    port = models.IntegerField(null=True, default=0)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        """
        Meta
        """
        db_table = 'work_station'
        verbose_name = 'Work Station'
        verbose_name_plural = 'Work Station'


class WorkUser(models.Model):
    """
    Model WorkUser
    """
    key = models.IntegerField(null=True, default=0)
    user_name = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        """
        Meta
        """
        db_table = 'work_user'
        verbose_name = 'Work User'
        verbose_name_plural = 'Work User'


class WorkProcess(models.Model):
    """
    Model WorkProcess
    """
    work_station = models.ForeignKey(WorkStation, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        """
        Meta
        """
        db_table = 'work_process'
        verbose_name = 'Work Process'
        verbose_name_plural = 'Work Process'
