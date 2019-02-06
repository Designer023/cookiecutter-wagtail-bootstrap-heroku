from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock, ChoiceBlock, StreamBlock, BooleanBlock

from .sub_component_streamfields import SUB_COMPONENT_STREAM_FIELDS

COLOR_NAMES = (
    (None, '---'),
    ('primary', 'Primary'),
    ('secondary', 'Secondary'),
    ('light', 'Light'),
    ('dark', 'Dark'),
    ('success', 'Success'),
    ('danger', 'Danger'),
    ('warning', 'Warning'),
    ('info', 'Info'),
)


class BootstrapBackground(StructBlock):
    background_theme = ChoiceBlock(choices=COLOR_NAMES, default='primary', required=False)


class BootstrapText(StructBlock):
    text_theme = ChoiceBlock(choices=COLOR_NAMES, default='dark', required=False)


class BootstrapStyleExtras(StructBlock):
    extra_classes = CharBlock(required=False)
    custom_styles = CharBlock(required=False)


class Bordered(StructBlock):
    border_theme = ChoiceBlock(choices=COLOR_NAMES, default=None, required=False)


class BootstrapCardBlock(BootstrapStyleExtras, Bordered, BootstrapText, BootstrapBackground):
    header = CharBlock(required=False)
    title = CharBlock(required=False)
    content = RichTextBlock(features=['p',])

    # content_list = StreamBlock(SUB_COMPONENT_STREAM_FIELDS)

    class Meta:
        icon = 'folder'
        template = 'global_utils/bootstrap_comonent_blocks/card.html'
        form_classname = 'struct-block'


class BootstrapAlertBlock(BootstrapBackground):
    title = CharBlock(required=False)
    content = RichTextBlock(features=['p',])
    dismissable = BooleanBlock(required=False)

    class Meta:
        icon = 'fa-exclamation-triangle'
        template = 'global_utils/bootstrap_comonent_blocks/alert.html'
        form_classname = 'struct-block'

