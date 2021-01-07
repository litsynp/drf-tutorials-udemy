from rest_framework import serializers

from status.models import Status


class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        # Do notice that these are almost the same as from `forms.py`.
        # However, DRF serializers serializes the data into JSON as well as validate them for you!
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

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
