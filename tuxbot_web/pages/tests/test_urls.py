import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_home():
    assert (reverse("pages:home") == "/")
    assert resolve("/").view_name == "pages:home"


def test_sources():
    assert (reverse("pages:sources") == "/sources/")
    assert resolve("/sources/").view_name == "pages:sources"


def test_contact():
    assert (reverse("pages:contact") == "/contact/")
    assert resolve("/contact/").view_name == "pages:contact"
