import pytest
from django.test import Client
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db

client = Client()


def test_home():
    assert reverse("pages:home") == "/"
    assert resolve("/").view_name == "pages:home"

    assert client.get(reverse("pages:home")).status_code == 200


def test_sources():
    assert reverse("pages:sources") == "/sources/"
    assert resolve("/sources/").view_name == "pages:sources"

    assert client.get(reverse("pages:sources")).status_code == 200


def test_contact():
    assert reverse("pages:contact") == "/contact/"
    assert resolve("/contact/").view_name == "pages:contact"

    assert client.get(reverse("pages:contact")).status_code == 200


def test_contact_post():
    assert client.post(reverse("pages:contact")).status_code == 400
    assert (
        client.post(
            reverse("pages:contact"),
            {
                "name": "John Doe",
                "email": "john@doe.fr",
                "message": "Hi there",
            },
        ).status_code
        == 200
    )
