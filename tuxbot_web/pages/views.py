from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.views.generic import View

from tuxbot_web.pages.forms import ContactForm

template_path = "pages/"


class HomeView(View):
    template_name = template_path + "home.html"

    def get(self, request: WSGIRequest):
        return render(request, self.template_name)


class SourcesView(View):
    template_name = template_path + "sources.html"

    def get(self, request: WSGIRequest):
        return render(request, self.template_name)


class ContactView(View):
    form_class = ContactForm
    template_name = template_path + "contact.html"

    def get(self, request: WSGIRequest):
        form = self.form_class(initial={"name": self.request.user.username})

        return render(request, self.template_name, {"form": form})

    def post(self, request: WSGIRequest):
        form = self.form_class(request.POST)

        if form.is_valid():
            messages.add_message(
                request, messages.SUCCESS, _("Message sent successfully")
            )
            form.save()

            form = self.form_class(
                initial={"name": self.request.user.username}
            )

            return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {"form": form})
