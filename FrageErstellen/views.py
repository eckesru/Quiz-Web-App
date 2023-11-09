from django.shortcuts import render, redirect
from Core.models import Frage, Modul, Tag
# from .models import KLASSENNAME, Hier Models importieren!

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def frage_erstellen_view(request):
    if request.method == 'POST':
        # Prüfen, ob es sich bei dem Aufruf um POST handelt
        user = request.user

        selected_tags_str_ids = request.POST.getlist('frageTags')
        selected_tags = Tag.objects.filter(str_id__in=selected_tags_str_ids)
        module_str_id = request.POST.get('frageModul')
        module = Modul.objects.get(str_id=module_str_id)

        title = request.POST.get('frageTitel')
        text = request.POST.get('frageText')

        # Erzeugung des Frage-Objekts
        frage = Frage.objects.create(
            user=user,
            module=module,
            title=title,
            text=text
        )

        # Hinzufügen der Tags zur Frage
        frage.tag.set(selected_tags)
        frage.save()

        return redirect("/frage/" + str(frage.id) + "/")
    module_choices = Modul.objects.all().values()
    tag_choices = Tag.objects.all().values()
    context = {"module_choices": module_choices, "tag_choices": tag_choices}
    return render(request, 'frage.html', context)
