import pytest

from tuxbot_web.pages.forms import ContactForm
from tuxbot_web.pages.tests.factories import ContactFactory

pytestmark = pytest.mark.django_db


class TestContactCreationForm:
    @staticmethod
    def test_clean_contact():
        # A contact with proto_contact params does not exist yet.
        proto_contact = ContactFactory.build()

        form = ContactForm(
            {
                "name": proto_contact.name,
                "email": proto_contact.email,
                "message": proto_contact.message,
            }
        )

        assert form.is_valid()

    @staticmethod
    def test_failed_contact():
        # A contact with proto_contact params does not exist yet.
        proto_contact = ContactFactory.build()

        form = ContactForm(
            {
                "name": proto_contact.name,
                "email": "42",
                "message": proto_contact.message,
            }
        )

        assert not form.is_valid()
