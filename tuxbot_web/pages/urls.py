from django.urls import path

from tuxbot_web.pages.views import HomeView, SourcesView, ContactView

app_name = "pages"
urlpatterns = [
    path("", view=HomeView.as_view(), name="home"),
    # path("wiki/", view=user_detail_view, name="wiki"),
    path("sources/", view=SourcesView.as_view(), name="sources"),
    path("contact/", view=ContactView.as_view(), name="contact"),
]
