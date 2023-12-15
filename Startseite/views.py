from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from Core.models import Frage, Benutzer, BenutzerQuesModel
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncDate, TruncTime
from django.utils import timezone
from django.core.paginator import Paginator
from .utils import get_hot_frage, get_frage_des_tages, get_top_5_users, \
                   get_user_answer_frage_des_tages, \
                   get_statistics_frage_des_tages


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
def startseite_view(request):
    if request.method == 'POST':
        reverse_url = request.META.get("HTTP_REFERER")
        if reverse_url is None:
            return redirect("/startseite/")
        return HttpResponseRedirect(reverse_url)

    del_user = Benutzer.objects.get(username="entfernt")

    # Sortierung des QuerySets. "-" bedeutet absteigend, "" aufsteigend.
    # TruncDate von Django holt nur Date, ignoriert Time.
    frage = Frage.objects.\
        exclude(user=del_user).\
        annotate(creation_date_only=TruncDate('creation_date'),
                 creation_time_only=TruncTime('creation_date')).\
        order_by("-creation_date_only", "-likes", "-creation_time_only")

    # Instanziierung eines Paginators
    # Damit werden Seiten von Django gemanaged
    # class Paginator(object_list, per_page, *orphans, *allow_empty_first_page)
    paginator = Paginator(frage, 10)
    page = request.GET.get('seite')
    page_frage = paginator.get_page(page)

    timestamp = timezone.localtime(timezone.now())

    hot_frage = get_hot_frage()

    frage_des_tages = get_frage_des_tages(request.user,
                                          timestamp)

    answer_user_frage_des_tages = get_user_answer_frage_des_tages(
                                  request.user,
                                  frage_des_tages,
                                  timestamp)

    answer_opt_frage_des_tages = frage_des_tages.get_option_by_value(
        frage_des_tages.ans)

    statistics_frage_des_tages = get_statistics_frage_des_tages(
        frage_des_tages, timestamp)

    top_5_user = get_top_5_users(timestamp)

    context = {"page_frage": page_frage,
               "hot_frage": hot_frage,
               "frage_des_tages": frage_des_tages,
               "answer_user_frage_des_tages": answer_user_frage_des_tages,
               "answer_opt_frage_des_tages": answer_opt_frage_des_tages,
               "statistics_frage_des_tages": statistics_frage_des_tages,
               "top_5_user": top_5_user,
               }

    return render(request, 'startseite.html', context)


@login_required(login_url='/login/-')
def update_answer_and_statistics(request):
    if request.method == 'POST':
        user = request.user

        timestamp = timezone.localtime(timezone.now())
        date = timestamp.date()

        frage_des_tages = get_frage_des_tages(request.user,
                                              timestamp)

        answer_user_frage_des_tages = get_user_answer_frage_des_tages(
                                      request.user,
                                      frage_des_tages,
                                      timestamp)

        if not answer_user_frage_des_tages:
            user_answer = request.POST.get('user_answer')

            # Antwort des Users in ManyToMany-Tabelle speichern
            user_answer_obj = BenutzerQuesModel.objects.create(
                date=date,
                user=user,
                quizfrage=frage_des_tages,
                answer=user_answer)

            user_answer_obj.save()

            # Aktualisieren der Punkte für den Ersteller
            Benutzer.update_points(user)

            statistics_frage_des_tages = get_statistics_frage_des_tages(
                frage_des_tages, timestamp)

            statistics_frage_des_tages['allowed'] = True

            return JsonResponse(statistics_frage_des_tages)

    return JsonResponse({'allowed': False})
