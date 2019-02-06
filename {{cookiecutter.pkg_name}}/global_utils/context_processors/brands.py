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
        brand_module = settings.BRAND_MODULE
    except AttributeError:
        brand_module = None


    if brand_module:
        brand_module_path = brand_module + "/"
    else:
        brand_module_path = ""

    try:
        brand_name = settings.BRAND_NAME
    except AttributeError:
        brand_name = None

    context = {
        'brand': {
            'environment_name': environment_name,
            'environment_color': environment_color,
            'brand_module': brand_module,
            'brand_module_path': brand_module_path,
            'brand_name': brand_name
        }
    }

    return context


