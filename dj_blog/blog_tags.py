from mezzanine.blog.templatetags import blog_tags as m_blogTags
from mezzanine import template

register = template.Library()

@register.as_tag
def blog_authors(parser, token):
    return m_blogTags.blog_authors(parser, token)

@register.as_tag
def blog_categories(parser, token):
    return m_blogTags.blog_categories(parser, token)

@register.as_tag
def blog_months(parser, token):
    return m_blogTags.blog_months(parser, token)

@register.as_tag
def blog_recent_posts(parser, token):
    return m_blogTags.blog_recent_posts( parser, token)

@register.inclusion_tag
def quick_blog(context):
    return m_blogTags.quick_blog(context)
