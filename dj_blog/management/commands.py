from mezzanine.blog.management import commands as m_commands
from m_commands.import_rss import Command as m_RSSCommand
from m_commands.import_blogger import Command as m_BloggerCommand
from m_commands.import_wordpress import Command as m_WordpressCommand
from m_commands.import_tumblr import Command as m_TumblrCommand

class RSSCommand(m_RSSCommand):
    def __init__(self, **kwargs):
        m_RSSCommand.__init__(self, **kwargs)

class BloggerCommand(m_BloggerCommand):
    def __init__(self, **kwargs):
        m_BloggerCommand.__init__(self, **kwargs)

class WordpressCommand(m_WordpressCommand):
    def __init__(self, **kwargs):
        m_WordpressCommand.__init__(self, **kwargs)

class TumblrCommand(m_TumblrCommand):
    def __init__(self, **kwargs):
        m_TumblrCommand.__init__(self, **kwargs)

def title_from_content(content):
    return m_TumblrCommand.title_from_content(content)
