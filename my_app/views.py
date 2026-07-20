# pyrefly: ignore [missing-import]
from django.shortcuts import render
import datetime

def home(request):
    context = {
        "title": "My Home Page",
    }

    context["date"] = datetime.datetime.today()
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": "About",
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
        "title": "Contact",
    }
    return render(request, "contact.html", context)
    