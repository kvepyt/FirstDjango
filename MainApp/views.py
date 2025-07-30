from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
#from MainApp.models import Item
#from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
author = {
        "name": "Валерий",
        "middle_name": "Евгеньевич",
        "last_name": "Косарев",
        "phone": "8-915-1111222",
        "email": "kve@kve60.ru",
    }
contact = {
    "name": "Косарев Валерий",
    "email": "kve@kve60.ru"
    }

full_contact = {
    "name": {author['name']},
    "Отчество": {author['middle_name']},
    "Фамилия": {author['last_name']},
    "Телефон": {author['phone']},
    "Почта": {author['email']},
}

    
items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity":10},
   {"id": 2, "name": "Куртка кожаная", "quantity":0},
   {"id": 3, "name": "Coca-cola 1 литр", "quantity":73},
   {"id": 4, "name": "Картофель фри", "quantity":152},
   {"id": 5, "name": "Кепка", "quantity":64},
]


def home(request) -> HttpResponse:
    return render(request, "index.html")


def about(request):
    context = {
        'author': author,
    }
    return render(request, "about.html", context)

"""По указанному id возвращает элемент из списка"""
def get_item(request, item_id: int):
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
                }
            return render (request,"item_page.html", context)
    return HttpResponseNotFound(f'<strong>Item with id={item_id} not found </strong>')
    

def get_items(request):
    context = {"items": items}
    return render(request, "items_list.html", context)