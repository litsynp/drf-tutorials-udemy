from rest_framework import serializers

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        # Do notice that these are almost the same as from `forms.py`.
        # However, DRF serializers serializes the data into JSON as well as validate them for you!
        model = Status
        fields = [
            'id',
            'content',
            'image',
            'uri',
        ]

    def get_uri(self, obj):
        return '/api/status/{id}/'.format(id=obj.id)


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)

    class Meta:
        # Do notice that these are almost the same as from `forms.py`.
        # However, DRF serializers serializes the data into JSON as well as validate them for you!
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri',
        ]
        read_only_fields = ['user']  # GET # readonly_fields

    def get_uri(self, obj):
        return '/api/status/{id}/'.format(id=obj.id)

    # Single field validation example:
    # def validate_<fieldname>(self, value):
    # For example,
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError('This is way too long.')
    #     return value

    def validate(self, data):
        """
        Validates all fields of Status model.
        """
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or image is required.')
        return data
