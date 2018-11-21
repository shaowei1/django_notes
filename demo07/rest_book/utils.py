from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework.status import HTTP_507_INSUFFICIENT_STORAGE
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError):
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': 'server inner error'}, status=HTTP_507_INSUFFICIENT_STORAGE)
        return response
