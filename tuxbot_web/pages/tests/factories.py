from factory import Faker
from factory.django import DjangoModelFactory

from tuxbot_web.pages.models import Contact


class ContactFactory(DjangoModelFactory):

    name = Faker("name")
    email = Faker("email")
    message = Faker("text")

    class Meta:
        model = Contact
        django_get_or_create = ["id"]
