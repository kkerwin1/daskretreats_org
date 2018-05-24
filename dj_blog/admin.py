from django.contrib import admin

# Register your models here.
from mezzanine.blog import admin as m_admin
from dj_blog.models import BlogPost, BlogCategory

class BlogCategoryAdmin(m_admin.BlogCategoryAdmin):
    def __init__(self, model, admin_site):
        m_admin.BlogCategoryAdmin.__init__(self, model, admin_site)

class BlogPostAdmin(m_admin.BlogPostAdmin):
    def __init__(self, *args, **kwargs):
        m_admin.BlogPostAdmin.__init__(self, *args, **kwargs)

admin.site.register(BlogPost, BlogCategory)
admin.site.register(BlogCategoryAdmin, BlogPostAdmin)
