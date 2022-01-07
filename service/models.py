# coding=utf-8

"""
Model Config
"""

from django.db import models

class WorkStation(models.Model):
    """Model WorkStation
    """
    key = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    port = models.IntegerField(null=True, default=0)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        """Meta
        """
        db_table = 'work_station'
        verbose_name = 'Work Station'
        verbose_name_plural = 'Work Station'


class WorkUser(models.Model):
    """Model WorkUser
    """
    company_data_id = models.IntegerField(null=True, default=0)
    corporate_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        """Meta
        """
        db_table = 'work_user'
        verbose_name = 'Work User'
        verbose_name_plural = 'Work User'


class WorkProcess(models.Model):
    """Model WorkProcess
    """
    work_user = models.ForeignKey(WorkUser, on_delete=models.SET_NULL, null=True)
    work_station = models.ForeignKey(WorkStation, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        """Meta
        """
        db_table = 'work_process'
        verbose_name = 'Work Process'
        verbose_name_plural = 'Work Process'
