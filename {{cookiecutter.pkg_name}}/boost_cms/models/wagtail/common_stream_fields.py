from wagtail.core.blocks import RawHTMLBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

from wagtailcodeblock.blocks import CodeBlock

from .bootstrap_components import BootstrapCardBlock, BootstrapAlertBlock


COMMON_STREAM_FIELDS = [
    ('richtext', RichTextBlock()),
    ('html', RawHTMLBlock()),
    ('code', CodeBlock()),
    ('image', ImageChooserBlock()),
    ('bootstrap_card', BootstrapCardBlock()),
    ('bootstrap_alert', BootstrapAlertBlock()),
]

