from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

template_path = "pages/"


class HomeView(View):
    template_name = template_path + "home.html"

    def get(self, request: WSGIRequest):
        return render(request, self.template_name)


class WikiView(View):
    template_name = template_path + "wiki/build/"

    def get(self, request: WSGIRequest, path=None):
        file_path = settings.ROOT_DIR / "tuxbot/templates"
        content_type = "text/html"

        if path is None:
            file_path /= self.template_name + "index.html"
        elif len(path.split('.')) == 1:
            file_path /= self.template_name + path + "/index.html"
        else:
            file_path /= self.template_name + path

            if (ext := path.split('.')[-1]) == "js":
                content_type = f"text/javascript"
            elif ext in ["svg", "png", "jpg", "jpeg"]:
                content_type = f"image/{ext}"
            else:
                content_type = f"text/{ext}"

        with open(file_path, "rb") as f:
            return HttpResponse(f.read(), content_type=content_type)
