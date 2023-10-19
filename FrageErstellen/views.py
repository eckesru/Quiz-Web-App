from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import KLASSENNAME # Hier Model importieren!
from Core.models import Frage


# Create your views here.
def frage(request):
    user = request.user
    username = user.username
    template = loader.get_template("frage.html")
    context = {
        "username": username,
    }
    return HttpResponse(template.render(context, request))
