from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class MediaStorage(S3Boto3Storage):
    # Import settings from the django
    location = settings.AWS_MEDIA_LOCATION
    file_overwrite = settings.AWS_FILE_OVERWRITE


class StaticStorage(S3Boto3Storage):
    # Import settings from the django
    location = settings.AWS_STATICFILES_LOCATION