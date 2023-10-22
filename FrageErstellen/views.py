from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# from .models import KLASSENNAME # Hier Model importieren!
from Core.models import Frage, Modul, Tag

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/') # Leitet User zum Login, wenn nicht eingeloggt


# Create your views here.
def frage(request):
    if request.method == 'POST': # Prüfen, ob es sich bei dem Aufruf um POST handelt
        user = request.user
        tags = request.POST.getlist('tags')
        tag_list = []
        for tag in tags:
            tag_list.append(Tag(tag.id, tag.str_id, tag.text))
        module = Modul(request.POST.get('modul.id'), request.POST.get('modul.str_id'), request.POST.get('modul.text'))
        title = request.POST.get('frageTitel')
        text = request.POST.get('frageText')
        frage = Frage(user=user, tags=tags, module=module, title=title, text=text)
        Frage.save(frage)
        return redirect("/FrageErstellen")
    module_choices = Modul.objects.all().values()
    tag_choices = Tag.objects.all().values()
    print(module_choices)
    print(tag_choices)
    context = {"module_choices": module_choices, "tag_choices": tag_choices}
    return render(request, 'frage.html', context)
