from mezzanine.blog import feeds as m_feeds

class PostsRSS(m_feeds.PostsRSS):
    def __init__(self, *args, **kwargs):
        m_feeds.PostsRSS.__init__(self, *args, **kwargs)

class PostsAtom(m_feeds.PostsAtom):
    def __init__(self, *args, **kwargs):
        m_feeds.PostsAtom.__init__(self, *args, **kwargs)
