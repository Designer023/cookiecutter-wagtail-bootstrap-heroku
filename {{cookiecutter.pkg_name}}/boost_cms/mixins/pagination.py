# from blog.models import BlogPost
from .. import app_settings as app_settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponseRedirect
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page


class PaginatedMixin(RoutablePageMixin):
    @route(r'^page/(?P<page_id>[0-9]+)/$', name='pagninated_index_page')
    def posts_by_page(self, request, page_id):
        self.page_id = int(page_id)

        if app_settings.PAGINATION_REDIRECT_INDEX_TO_ROOT:
            # Redirects to the root page if the page index is 1
            if self.page_id == 1:
                # Redirects to the index page if the page id is 1
                return HttpResponseRedirect(self.url)
            else:
                # Returns the page index as long as it's not 1
                return Page.serve(self, request)
        else:
            # Serves the page 1
            return Page.serve(self, request)

    @route(r'^$', name='pagninated_index')
    def post_list(self, request, *args, **kwargs):
        self.page_id = 1

        if app_settings.PAGINATION_REDIRECT_INDEX_TO_ROOT:
            # Return the index page
            return Page.serve(self, request, *args, **kwargs)
        else:
            # redirect to /page/1/
            return HttpResponseRedirect(self.reverse_subpage('pagninated_index_page', args=(1,)))

    def get_child_page_queryset(self):
        return Page.objects.child_of(self).live().order_by('-first_published_at').specific()
        # return self.get_children().live().order_by('-first_published_at')

    def get_child_page_size(self, request):
        # Get the page size from a query string or use the default size
        return int(request.GET.get(
            'page_size',
            app_settings.PAGINATION_PAGE_SIZE_DEFAULT
        ))

    def get_context(self, request, *args, **kwargs):
        context = super(PaginatedMixin, self).get_context(request, *args, **kwargs)

        child_pages = self.get_child_page_queryset()

        tag_list = None
        category_list = None

        # Filter by tag
        tag = request.GET.get('tag')

        if tag:
            tag_list = [x.strip() for x in tag.split(',')]
            child_pages = child_pages.filter(blogpost__tags__slug__in=tag_list).distinct()

        category = request.GET.get('category')
        if category:
            category_list = [x.strip() for x in category.split(',')]
            child_pages = child_pages.filter(blogpost__categories__slug__in=category_list).distinct()

        current_page_size = self.get_child_page_size(request)
        context['current_page_size'] = current_page_size

        paginator = Paginator(child_pages, current_page_size)

        page = self.page_id

        try:
            paginated_objects = paginator.page(page)
        except PageNotAnInteger:
            raise Http404()
        except EmptyPage:
            raise Http404()

        context['paginated_objects'] = paginated_objects
        context['tag_list'] = tag_list
        context['category_list'] = category_list

        return context