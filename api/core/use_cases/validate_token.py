from django.conf import settings
from rest_framework.response import Response
import jwt


def validateToken(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        if(decoded_token):
            return True
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None