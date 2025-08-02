from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

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


def home(request) -> HttpResponse:
    return render(request, "index.html")


def about(request):
    context = {
        'author': author,
    }
    return render(request, "about.html", context)


"""По указанному id возвращает элемент из списка"""


def get_item(request, item_id: int):
    """TODO: get item my id from db """
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {'errors': [f'Item with id={item_id} not found']})
    else:
        colors = item.colors.all()
        context = {
            "item": item,
            "colors": colors,
        }
    return render(request, "item_page.html", context)


def get_items(request):
    """TODO: get all itemsfrom db """
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)
