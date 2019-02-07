from .base import *
import os

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')
SITE_HOST_URL = os.getenv('SITE_HOST_URL')

ALLOWED_HOSTS = [SITE_HOST_URL]

STATIC_URL = '/static/'

AWS_MEDIA_LOCATION = 'media'
AWS_STATICFILES_LOCATION = 'static'
AWS_FILE_OVERWRITE = True

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')

AWS_IS_GZIPPED = True

GZIP_CONTENT_TYPES = (
    'text/css',
    'application/javascript',
    'application/x-javascript',
    'text/javascript',
    'image/svg+xml'
)

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}


MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'global_utils.storages.backends.MediaStorage'
STATICFILES_STORAGE = 'global_utils.storages.backends.StaticStorage'

WEBPACK_STATIC_PATH='prod/'

AWS_QUERYSTRING_AUTH = False

try:
    from .local import *
except ImportError:
    pass
