from mezzanine.blog import forms as m_forms

class BlogPostForm(m_forms.BlogPostForm):
    def __init__(self):
        m_forms.BlogPostForm.__init__(self)
