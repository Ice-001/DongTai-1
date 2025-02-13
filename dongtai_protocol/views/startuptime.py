######################################################################
# @author      : bidaya0 (bidaya0@$HOSTNAME)
# @file        : startuptime
# @created     : 星期三 10月 20, 2021 16:07:48 CST
#
# @description :
######################################################################



import logging

from dongtai_common.models.agent import IastAgent
from dongtai_common.models.agent_properties import IastAgentProperties
from rest_framework.request import Request

from dongtai_common.endpoint import OpenApiEndPoint, R
from dongtai_protocol.serializers.agent_properties import AgentPropertiesSerialize
import time
from dongtai_protocol.api_schema import DongTaiParameter, DongTaiAuth
from drf_spectacular.utils import extend_schema
from dongtai_protocol.decrypter import parse_data
from django.http.request import QueryDict

logger = logging.getLogger("django")


class StartupTimeEndPoint(OpenApiEndPoint):
    name = "api-v1-startuptime"

    @extend_schema(description='Agent Limit', auth=[DongTaiAuth.TOKEN])
    def post(self, request: Request):
        agent_id = request.data.get('agentId', None)
        startup_time = request.data.get('startupTime', None)
        agent = IastAgent.objects.filter(pk=agent_id).first()
        if agent:
            agent.startup_time = startup_time
            agent.save(update_fields=['startup_time'])
            return R.success(data=None)
        logger.error('agent not found')
        return R.failure(data=None)


class StartupTimeGzipEndPoint(StartupTimeEndPoint):
    name = "api-v1-startuptime"

    @extend_schema(description='Agent Limit', auth=[DongTaiAuth.TOKEN])
    def post(self, request: Request):
        try:
            param = parse_data(request.read())
            request._full_data = param
            return super().post(request)
        except Exception as e:
            logger.info(e)
            return R.failure(data=None)
