from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import View


template_path = "pages/"


class HomeView(View):
    template_name = template_path + "home.html"

    def get(self, request: WSGIRequest):
        return render(request, self.template_name)


class WikiView(View):
    template_name = template_path + "wiki.html"

    def get(self, request: WSGIRequest):
        return render(request, self.template_name)
