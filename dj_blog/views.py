# Create your views here.
from __future__ import unicode_literals
from future.builtins import str
from future.builtins import inclusion_tag
from calendar import month_name

from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404

from dj_blog.models import BlogPost, BlogCategory
from dj_blog.feeds import PostsRSS, PostsAtom
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render, paginate

User = get_user_model()

def blog_post_list(request, tag=None, year=None, month=None, poster=None,
                   category=None, template=u'blog/blog_post_list.html',
                   extra_context=None, author=None, guest_author=None
                   ):
    """
    Display a list of blog posts that are filtered by tag, year, month,
    author, or category. Custom templates are checked for using the name
    'blog/blog_post_list/XXX/' where 'XXX' is either the category slug
    or author's username if given.

    Local re-write of mezzanine.blog.views.blog_post_list().
    """

    prefetch = ("categories", "keywords__keyword")

    templates = []
    blog_posts = BlogPost.objects.published(for_user=request.user)
    if tag is not None:
        tag = get_object_or_404(Keyword, slug=tag)
    if year is not None:
        blog_posts = blog_posts.filter(publish_date__year=year)
        if month is not None:
            blog_posts = blog_posts.filter(publish_date__month=month)
            try:
                month = month_name[int(month)]
            except IndexError:
                raise Http404()
    if category is not None:
        category = get_object_or_404(BlogCategory, slug=category)
        blog_posts = blog_posts.filter(categories=category)
        templates.append(u'blog/blog_post_list/by-category/%s/'
                        % str(category.slug))
    if author is not None:
        author = get_object_or_404(User, username=author)
        blog_posts = blog_posts.filter(author=author)
        blog_posts = blog_posts.select_related("author").prefetch_related(*prefetch)
        templates.append(u'blog/blog_post_list/by-author/%s/ % author)
    if poster is not None:
        poster = get_object_or_404(user, username=poster)
        blog_posts = blog_posts.filter(poster=poster)
        blog_posts = blog_posts.select_related("poster").prefetch_related(*prefetch)
        templates.append(u'blog/blog_post_list/by-poster/%s/ % poster)
    if guest_author is not None:
        blog_posts = blog_posts.filter(guest_author)
        blog_posts = blog_posts.select_related("guest_author").prefetch_related(*prefetch)
        templates.append(u'blog/blog_post_list/by-guest_author/%s/
                        % guest_author)

    blog_posts = paginate(blog_posts, request.GET.get('page, 1'),
                         settings.BLOG_POST_PER_PAGE,
                         settings.MAX_PAGING_LINKS)
    context = {"blog_posts": blog_posts, "year": year, "month": month,
               "tag": tag, "category": category, "author": author,
               "poster": poster, "guest_author": guest_author}
    context.update(extra_context or {})
    templates.append(template)
    return render(request, templates, context)


#-----

def blog_post_detail(request, slug, year=None, month=None, day=None,
                    template=u'blog/blog_post_detail.html",
                    extra_context=None
                    ):
    return m_views.blog_post_detail(request, slug, year, month, day,
                                    template, extra_context
                                    )

def blog_post_feed(request, format, **kwargs):
    return m_views.blog_post_feed(request, format, **kwargs)

def blog_post_list(request, tag=None, year=None, month=None, username=None,
                   category=None, template=u'blog/blog_post_list.html',
                   extra_context=None
                   )
    return m_views.blog_post_list(request, tag, year, month, username,
                                  category, template, extra_context
                                  )
