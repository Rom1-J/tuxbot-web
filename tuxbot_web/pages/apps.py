from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PagessConfig(AppConfig):
    name = "tuxbot_web.pages"
    verbose_name = _("Pages")

    def ready(self):
        try:
            import tuxbot_web.pages.signals  # noqa F401
        except ImportError:
            pass
