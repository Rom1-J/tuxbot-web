from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "tuxbot_web.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            # pylint: disable=import-outside-toplevel
            # pylint: disable=unused-import
            import tuxbot_web.users.signals  # noqa F401
        except ImportError:
            pass
