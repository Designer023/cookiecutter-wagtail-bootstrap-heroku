from django.db import models
from django.forms.widgets import CheckboxSelectMultiple

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet


from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag as TaggitTag

from ..mixins.pagination import PaginatedMixin

from .wagtail.stream_fields import TOP_LEVEL_STREAM_FIELDS


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('boost_cms.BlogPost', on_delete=models.CASCADE, related_name='tagged_items')

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

class BlogLanding(PaginatedMixin, Page):

    subpage_types = ['boost_cms.BlogPost']

    template="blog/blog_landing.html"

    def get_context(self, request, *args, **kwargs):
        context = super(BlogLanding, self).get_context(request, *args, **kwargs)

        return context

class BlogPost(Page):

    parent_page_types = ['boost_cms.BlogLanding']

    template="blog/blog_post.html"

    date = models.DateTimeField("Post date")

    sub_title = models.CharField(
        blank=True,
        null=True,
        max_length=256,
        help_text="Subtext to appear on page styles that support sub-headings"
    )

    page_body = StreamField(TOP_LEVEL_STREAM_FIELDS)

    categories = ParentalManyToManyField('boost_cms.BlogCategory', blank=True)

    tags = ClusterTaggableManager(through='boost_cms.BlogPageTag', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('sub_title'),
        StreamFieldPanel('page_body'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
        FieldPanel('categories', widget=CheckboxSelectMultiple),
    ]
