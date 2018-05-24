from __future__ import unicode_literals

from django.db import models

# Create your models here.

from mezzanine.blog import models as m_models

class BlogCategory(m_models.BlogCategory):
    def __init__(self, *args, **kwargs):
        m_models.BlogCategory.__init__(self, *args, **kwargs)

class BlogPost(m_models.BlogPost):
    def __init(self, *args, **kwargs):
        m_models.BlogPost.__init__(self, *args, **kwargs)
