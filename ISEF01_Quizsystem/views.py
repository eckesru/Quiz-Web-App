from django.shortcuts import redirect


# Homepage. Redirect zur Startseite.
def home_view(request):
    return redirect("/startseite/")
