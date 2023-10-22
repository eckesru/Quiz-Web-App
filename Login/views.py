import time
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # Authentifiziert den User
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login erfolgreich.')
            time.sleep(2)
            return redirect("/frage-erstellen/")
        else:
            messages.error(request, 'Login fehlgeschlagen')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
