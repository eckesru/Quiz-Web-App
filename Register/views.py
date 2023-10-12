from django.shortcuts import render, redirect
from .forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/Login/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
