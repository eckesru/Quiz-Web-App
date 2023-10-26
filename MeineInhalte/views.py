from django.shortcuts import render, redirect
from Core.models import Frage, Modul, Tag
# from .models import KLASSENNAME, Hier Models importieren!

from django.contrib.auth.decorators import login_required
# Zur Umleitung auf /login/ benötigt


@login_required(login_url='/login/')
# Leitet User zum Login, wenn nicht eingeloggt
# Create your views here.
def meine_inhalte_view(request):
    user = request.user
    if request.method == 'POST':
        
        return redirect("/frage-erstellen/")
    user_fragen = Frage.objects.filter(user_id=user)
    context = {"fragen": user_fragen}
    return render(request, 'meineInhalte.html', context)
    
def delete_question(request):
    frage_del = request.POST.get('frage')
    frage_del_obj = Frage.objects.filter(id=frage)
    frage_del_obj.delete()
    return render(request, 'meineInhalte.html')
    
def edit_question(request):
    frage_edit = request.POST.get('frage')
    frage_edit_obj = Frage.objects.filter(id=frage)
    context = {"frage": frage}
    return render(request, 'meineInhalte.html', context)
