import datetime

from django.utils import timezone
from rest_framework_jwt.settings import api_settings

# Get the JWT expiration delta from settings.py
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


# Change the response of obtain_jwt_token on issuing JWT
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    }
