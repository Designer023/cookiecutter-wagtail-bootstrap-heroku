from .common_stream_fields import COMMON_STREAM_FIELDS
from .grid_fields import GridRow


GRID_STREAM_FIELDS = [
    ('row', GridRow()),
]


TOP_LEVEL_STREAM_FIELDS = []

TOP_LEVEL_STREAM_FIELDS += GRID_STREAM_FIELDS
TOP_LEVEL_STREAM_FIELDS += COMMON_STREAM_FIELDS

