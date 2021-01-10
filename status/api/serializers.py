from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField, PrimaryKeyRelatedField
from rest_framework.reverse import reverse as api_reverse

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    # # user_id = PrimaryKeyRelatedField(source='user', read_only=True)
    # # user_uri = HyperlinkedRelatedField(
    # #     source='user',  # user foreign key
    # #     lookup_field='username',
    # #     view_name='user-detail',
    # #     read_only=True)
    # user = serializers.SlugRelatedField(read_only=True, slug_field='username')

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
        request = self.context.get('request')
        return api_reverse('status-detail', kwargs={'pk': obj.id}, request=request)

    def get_user(self, obj):
        request = self.context.get('request')
        user = obj.user
        return UserPublicSerializer(user, read_only=True, context={'request': request}).data

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


class StatusInlineUserSerializer(StatusSerializer):
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
        request = self.context.get('request')
        return api_reverse('status-detail', kwargs={'pk': obj.id}, request=request)

# class StatusInlineUserSerializer(StatusSerializer):
#     uri = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         # Do notice that these are almost the same as from `forms.py`.
#         # However, DRF serializers serializes the data into JSON as well as validate them for you!
#         model = Status
#         fields = [
#             'id',
#             'content',
#             'image',
#             'uri',
#         ]

#     def get_uri(self, obj):
#         request = self.context.get('request')
#         return api_reverse('status-detail', kwargs={'pk': obj.id}, request=request)
