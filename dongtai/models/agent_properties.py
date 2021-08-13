#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/1/14 下午2:54
# software: PyCharm
# project: dongtai-models
from django.db import models
import os

from dongtai.models.agent import IastAgent


class IastAgentProperties(models.Model):
    hook_type = models.IntegerField(blank=True, null=True)
    dump_class = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    agent = models.ForeignKey(IastAgent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True if os.getenv('environment',None) == 'TEST' else False
        db_table = 'iast_agent_properties'
