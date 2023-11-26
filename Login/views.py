from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        # Authentifiziert den User
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Eigene AuthenticationForm, um Fehlermeldungen anzupassen
class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Ungültiger Benutzer oder ungültiges Passwort."
        ),
        'inactive': _("Benutzer ist inaktiv."),
    }
