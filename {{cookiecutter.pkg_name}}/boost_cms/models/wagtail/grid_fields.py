from wagtail.core.blocks import StructBlock, StreamBlock, IntegerBlock

from .common_stream_fields import COMMON_STREAM_FIELDS

class ColSpan(StructBlock):
    xs = IntegerBlock(required=False, min_value=1, max_value=12, default=12 )
    sm = IntegerBlock(required=False, min_value=1, max_value=12)
    md = IntegerBlock(required=False, min_value=1, max_value=12)
    lg = IntegerBlock(required=False, min_value=1, max_value=12)
    xl = IntegerBlock(required=False, min_value=1, max_value=12)

    class Meta:
        form_template = 'global_utils/forms/column_form.html'

class ColOffset(StructBlock):
    xs = IntegerBlock(required=False, min_value=0, max_value=11)
    sm = IntegerBlock(required=False, min_value=0, max_value=11)
    md = IntegerBlock(required=False, min_value=0, max_value=11)
    lg = IntegerBlock(required=False, min_value=0, max_value=11)
    xl = IntegerBlock(required=False, min_value=0, max_value=11)

    class Meta:
        form_template = 'global_utils/forms/column_form.html'


class ColOrder(StructBlock):
    xs = IntegerBlock(required=False, min_value=-1, max_value=13)
    sm = IntegerBlock(required=False, min_value=-1, max_value=13)
    md = IntegerBlock(required=False, min_value=-1, max_value=13)
    lg = IntegerBlock(required=False, min_value=-1, max_value=13)
    xl = IntegerBlock(required=False, min_value=-1, max_value=13)

    class Meta:
        form_template = 'global_utils/forms/column_form.html'


class ColumnComponent(StructBlock):
    columns = ColSpan()
    offset = ColOffset()
    order = ColOrder()

    content = StreamBlock(COMMON_STREAM_FIELDS)

COLUMN_COMPONENT_FIELDS = [
    ('column', ColumnComponent()),
    # Todo: Add .w-100 class block for breaking columns
    # see: https://getbootstrap.com/docs/4.2/layout/grid/
]

class GridRow(StructBlock):

    content_list = StreamBlock(COLUMN_COMPONENT_FIELDS)

    class Meta:
        icon = 'fa-columns'
        template = 'global_utils/bootstrap_comonent_blocks/card.html'