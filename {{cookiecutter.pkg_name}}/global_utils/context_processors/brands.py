# import socket

from django.conf import settings

def context(request):

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
            'brand_module': brand_module,
            'brand_module_path': brand_module_path,
            'brand_name': brand_name
        }
    }

    return context


