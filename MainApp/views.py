from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request) -> HttpResponse:
    context = {
        "name": "Косарев Валерий",
        "email": "kve@kve60.ru"
    }
    return render(request, "index.html", context)

