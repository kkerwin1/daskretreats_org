from django.shortcuts import render

# Create your views here.

from mezzanine.blog import views as m_views

def blog_post_detail(
    request, slug, year=None, month=None, day=None,
        template=u'blog/blog_post_detail.html", extra_context=None
        ):
    return m_views.blog_post_detail(request, slug, year, month, day,
        template, extra_context
        )

def blog_post_feed(request, format, **kwargs):
    return m_views.blog_post_feed(request, format, **kwargs)

def blog_post_list(
    request, tag=None, year=None, month=None, username=None, category=None,
        template=u'blog/blog_post_list.html', extra_context=None
        )
    return m_views.blog_post_list(request, tag, year, month, username,
        category, template, extra_context
        )
