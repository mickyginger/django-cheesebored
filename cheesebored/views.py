import os
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponse

class Home(View):

    def get(self, _request):
        with open(os.path.join(settings.BASE_DIR, 'dist', 'index.html')) as file:
            return HttpResponse(file.read())
