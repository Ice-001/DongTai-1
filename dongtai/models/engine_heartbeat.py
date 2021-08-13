#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: owefsad@huoxian.cn
# datetime: 2021/5/6 下午5:56
# project: dongtai-models
from django.db import models
import os


class IastEngineHeartbeat(models.Model):
    client_ip = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    agentcount = models.IntegerField(db_column='agentCount', blank=True, null=True)  # Field name made lowercase.
    reqcount = models.BigIntegerField(db_column='reqCount', blank=True, null=True)  # Field name made lowercase.
    agentenablecount = models.IntegerField(db_column='agentEnableCount', blank=True,
                                           null=True)  # Field name made lowercase.
    projectcount = models.IntegerField(db_column='projectCount', blank=True, null=True)  # Field name made lowercase.
    usercount = models.IntegerField(db_column='userCount', blank=True, null=True)  # Field name made lowercase.
    vulcount = models.IntegerField(db_column='vulCount', blank=True, null=True)  # Field name made lowercase.
    methodpoolcount = models.IntegerField(db_column='methodPoolCount', blank=True,
                                          null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True if os.getenv('environment',None) == 'TEST' else False
        db_table = 'iast_engine_heartbeat'
