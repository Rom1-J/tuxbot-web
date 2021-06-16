from django.urls import path, re_path
from django.views.generic import RedirectView

from tuxbot.pages.views import HomeView, WikiView

app_name = "pages"
urlpatterns = [
    path("", view=HomeView.as_view(), name="home"),

    path("wiki/", view=WikiView.as_view(), name="wiki"),
    re_path(r"^wiki/(?P<path>[a-zA-Z0-9/\.~\-]+)$", view=WikiView.as_view(), name="wiki"),

    path("support/",
         view=RedirectView.as_view(url='https://discord.gg/URKy7yd'),
         name="support"),
    path("sources/",
         view=RedirectView.as_view(url='https://github.com/Rom1-J/tuxbot-bot'),
         name="sources"),
]
