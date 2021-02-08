import pytest
from django.test import RequestFactory

from tuxbot_web.users.api.views import UserViewSet
from tuxbot_web.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    @staticmethod
    def test_get_queryset(user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    @staticmethod
    def test_me(user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": user.username,
            "email": user.email,
            "name": user.name,
            "url": f"http://testserver/api/users/{user.username}/",
        }
