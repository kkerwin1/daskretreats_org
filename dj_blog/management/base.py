from mezzanine.blog.management import base as m_base:

class BaseImporterCommand(m_base.BaseImporterCommand):
    def __init__(self, **kwargs):
        m_base.BaseImporterCommand.__init__(self, **kwargs)
