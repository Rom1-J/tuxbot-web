import pytest

from tuxbot_web.users.forms import UserCreationForm
from tuxbot_web.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    @staticmethod
    def test_clean_username():
        # A user with proto_user params does not exist yet.
        proto_user = UserFactory.build()

        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,  # pylint: disable=protected-access
                "password2": proto_user._password,  # pylint: disable=protected-access
            }
        )

        assert form.is_valid()
        assert form.clean_username() == proto_user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,  # pylint: disable=protected-access
                "password2": proto_user._password,  # pylint: disable=protected-access
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors
