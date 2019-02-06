from wagtail.core.blocks import RawHTMLBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

from wagtailcodeblock.blocks import CodeBlock


SUB_COMPONENT_STREAM_FIELDS = [
    ('richtext', RichTextBlock()),
    ('html', RawHTMLBlock()),
    ('code', CodeBlock()),
    ('image', ImageChooserBlock()),
]

