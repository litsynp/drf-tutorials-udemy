from rest_framework import serializers

from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        # Do notice that these are almost the same as from `forms.py`.
        # However, DRF serializers serializes the data into JSON as well as validate them for you!
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]
