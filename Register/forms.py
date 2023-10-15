from django import forms
from django.contrib.auth.forms import UserCreationForm
from Core.models import Benutzer


class RegisterForm(UserCreationForm):
    class Meta:
        model = Benutzer
        fields = ["username", "password1", "password2", "email", "first_name",
                  "last_name"]
