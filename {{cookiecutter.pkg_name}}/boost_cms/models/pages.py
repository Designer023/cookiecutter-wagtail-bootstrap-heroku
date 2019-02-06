from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from django.db import models

from wagtail.core.fields import StreamField, RichTextField

from .wagtail.stream_fields import TOP_LEVEL_STREAM_FIELDS


PAGE_TYPE_CHOICES = (
    (None, 'Default'),
    ('cover', 'Cover'),
)

class BasicPage(Page):

    sub_title = models.CharField(
        blank=True,
        null=True,
        max_length=256,
        help_text="Subtext to appear on page styles that support sub-headings"
    )

    page_body = StreamField(TOP_LEVEL_STREAM_FIELDS)

    page_type = models.CharField(
        choices=PAGE_TYPE_CHOICES,
        default=None,
        blank=True,
        null=True,
        max_length=56
    )

    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        StreamFieldPanel('page_body'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('page_type'),
    ]


    def get_template(self, request, *args, **kwargs):

        if self.page_type and self.page_type == 'cover':
            return "pages/cover_page.html"

        else:
            return "pages/basic_page.html"
