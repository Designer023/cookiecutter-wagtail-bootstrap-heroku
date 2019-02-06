from .base import *
import os

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')
SITE_HOST_URL = os.getenv('SITE_HOST_URL')

ALLOWED_HOSTS = [SITE_HOST_URL]

AWS_MEDIA_LOCATION = 'media'
AWS_STATICFILES_LOCATION = 'static'
AWS_FILE_OVERWRITE = True

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'global_utils.storages.backends.MediaStorage'
STATICFILES_STORAGE = 'global_utils.storages.backends.StaticStorage'

try:
    from .local import *
except ImportError:
    pass
