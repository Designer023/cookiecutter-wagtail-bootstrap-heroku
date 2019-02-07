# import socket

from django.conf import settings

def context(request):

    try:
        environment_name = settings.ENVIRONMENT_NAME
    except AttributeError:
        environment_name = 'Development'

    try:
        environment_color = settings.ENVIRONMENT_COLOR
    except AttributeError:
        environment_color = '#ffffff'

    try:
        webpack_static = settings.WEBPACK_STATIC_PATH
    except AttributeError:
        webpack_static = 'prod/'

    context = {
        'environment': {
            'environment_name': environment_name,
            'environment_color': environment_color,
            'webpack_static': webpack_static
        }
    }

    return context


