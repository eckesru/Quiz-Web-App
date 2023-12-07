from django.shortcuts import render
from Core.models import Frage, Antwort
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def meine_inhalte_view(request):
    user = request.user

    user_fragen = Frage.objects.filter(user_id=user).\
        order_by("-creation_date")

    # Instanziierung des Paginators
    # class Paginator(object_list, per_page, *orphans, *allow_empty_first_page)
    paginator_frage = Paginator(user_fragen, 10)

    page_frage = request.GET.get('seite')
    # Aufbau: .../?seite=x-y, split um x zu bekommen
    page_frage_list = page_frage.split("-")
    page_frage_obj = paginator_frage.get_page(page_frage_list[0])

    user_antworten = Antwort.objects.filter(user_id=user).\
        order_by("-creation_date")

    # Instanziierung des Paginators
    # class Paginator(object_list, per_page, *orphans, *allow_empty_first_page)
    paginator_antwort = Paginator(user_antworten, 15)

    page_antwort = request.GET.get('seite')
    # Aufbau: .../?seite=x-y, split um y zu bekommen
    page_antwort_list = page_antwort.split("-")
    page_antwort_obj = paginator_antwort.get_page(page_antwort_list[1])

    context = {"page_frage": page_frage_obj, "page_antwort": page_antwort_obj}
    return render(request, 'meineInhalte.html', context)
