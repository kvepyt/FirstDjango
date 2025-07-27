from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
author = {
        "name": "Валерий",
        "middle_name": "Евгеньевич",
        "last_name": "Косарев",
        "phone": "8-915-1111222",
        "email": "kve@kve60.ru",
    }

def home(request):
    text = """"
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Косарев В.Е.</i>
    """
    return HttpResponse(text)

def about(request):
    context = f"""
    Имя: {author['name']} <br>
    Отчество: {author['middle_name']} <br>
    Фамилия: {author['last_name']} <br>
    Телефон: {author['phone']} <br>
    Почта: {author['email']} <br>
"""
    return HttpResponse(context)
