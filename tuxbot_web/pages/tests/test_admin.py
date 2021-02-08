import pytest
from django.urls import reverse

from tuxbot_web.pages.models import Contact

pytestmark = pytest.mark.django_db


class TestContactAdmin:
    @staticmethod
    def test_changelist(admin_client):
        url = reverse("admin:pages_contact_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    @staticmethod
    def test_search(admin_client):
        url = reverse("admin:pages_contact_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    @staticmethod
    def test_add(admin_client):
        url = reverse("admin:pages_contact_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "name": "John Doe",
                "email": "john@doe.fr",
                "message": "This is a message",
            },
        )
        assert response.status_code == 302
        assert Contact.objects.filter(email="john@doe.fr").exists()
