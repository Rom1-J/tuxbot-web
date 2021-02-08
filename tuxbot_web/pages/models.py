from django.db import models
from django.db.models import (
    CharField,
    EmailField,
    TextField,
    DateTimeField,
    BooleanField,
)
from django.db.models.fields import AutoField
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(_("Name"), blank=False, max_length=255)
    email = EmailField(_("Email"), blank=False)
    message = TextField(_("Message"), blank=False)

    created_at = DateTimeField(auto_now_add=True)

    read = BooleanField(_("Read"), default=False)
    answered = BooleanField(_("Answered"), default=False)
