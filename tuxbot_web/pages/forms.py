from django.forms import ModelForm

from django.utils.translation import gettext_lazy as _
from tuxbot_web.pages.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

        labels = {
            "name": _("Your name"),
            "email": _("Your email"),
            "message": _("Your message"),
        }

    def is_valid(self):
        result = super().is_valid()
        # loop on *all* fields if key '__all__' found else only on errors:
        for x in self.fields if "__all__" in self.errors else self.errors:
            attrs = self.fields[x].widget.attrs
            attrs.update({"class": attrs.get("class", "") + " form-error"})
        return result
