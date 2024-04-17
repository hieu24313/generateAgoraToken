"""Stream views"""
import uuid

# djangoREST
from rest_framework.views import APIView
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from stream_control.serializers import StreamTokenSerializer
from stream_control.models import StreamTokenUser
from stream_control.utils import get_tokenrtc

# Create your views here.
import sys
import os
import time
from random import randint
from datetime import datetime

appID = "6d5049b6ee13472197020fe7c3117e6c"
appCertificate = "8e9f6ae6a2aa4097b2c4f11dd81178c9"
channelName = "call"
expireTimeInSeconds = 3600000
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expireTimeInSeconds


def generate_random_uuid():
    # Tạo một UUID ngẫu nhiên (phiên bản 4)
    random_uuid = uuid.uuid4()
    return str(random_uuid)


class StreamTokenViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Users ViewSet"""
    queryset = StreamTokenUser.objects.all()
    serializer_class = StreamTokenSerializer
    lookup_field = 'id_user'

    def get_permissions(self):
        permissions = [AllowAny]
        return [permission() for permission in permissions]

    @action(detail=False, methods=['get'])
    def generate_token(self, request):
        """
            Roles users
            0 =
            1 =
            2 =
        """

        id_user = generate_random_uuid()
        token_rtc = get_tokenrtc(
            appID, appCertificate, channelName, id_user,
            0, expireTimeInSeconds, currentTimestamp, privilegeExpiredTs
        )
        data = {
            "tokenRTC": token_rtc,
            "uid": id_user
        }
        return Response(data, status=status.HTTP_201_CREATED)
