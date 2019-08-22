import os
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound

class Home(View):

    def get(self, _request):
        with open(os.path.join(settings.BASE_DIR, 'dist', 'index.html')) as file:
            return HttpResponse(file.read())


class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(settings.BASE_DIR, 'dist', filename)

        if os.path.isfile(path):
            with open(path) as file:
                return HttpResponse(file.read())

        else:
            return HttpResponseNotFound()
