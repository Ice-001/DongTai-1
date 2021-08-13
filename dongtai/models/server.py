#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2020/5/25 14:47
# software: PyCharm
# project: dongtai-models
from django.db import models
import os


class IastServer(models.Model):
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    container = models.CharField(max_length=255, blank=True, null=True)
    container_path = models.CharField(max_length=255, blank=True, null=True)
    command = models.CharField(max_length=255, blank=True, null=True)
    env = models.CharField(max_length=255, blank=True, null=True)
    runtime = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    network = models.CharField(max_length=255, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True if os.getenv('environment',None) == 'TEST' else False
        db_table = 'iast_server'
