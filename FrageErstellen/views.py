from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import KLASSENNAME # Hier Model importieren!!


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {
        "name": "Jambo",
    }
    return HttpResponse(template.render(context, request))
