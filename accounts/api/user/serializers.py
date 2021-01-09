import datetime

from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers

from status.api.serializers import StatusInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status',
        ]

    def get_uri(self, obj):
        return '/api/users/{id}/'.format(id=obj.id)

    def get_status(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.status_set.all().order_by('-timestamp')
        data = {
            'url': self.get_uri(obj) + 'status/',
            'last': StatusInlineUserSerializer(qs.first()).data,
            'recent': StatusInlineUserSerializer(qs[:limit], many=True).data
        }
        return data
