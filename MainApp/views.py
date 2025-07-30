from django.http import HttpResponse, HttpResponseNotFound
#from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
author = {
        "name": "Валерий",
        "middle_name": "Евгеньевич",
        "last_name": "Косарев",
        "phone": "8-915-1111222",
        "email": "kve@kve60.ru",
    }
items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity":10},
   {"id": 2, "name": "Куртка кожаная", "quantity":42},
   {"id": 3, "name": "Coca-cola 1 литр", "quantity":73},
   {"id": 4, "name": "Картофель фри", "quantity":152},
   {"id": 5, "name": "Кепка", "quantity":64},
]

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Косарев В.Е.</i>
    <br>
    <br>
    <a href = "/about">About</a>
    <br>
    <br>
    <a href = "/items">Список товаров</a>
    """
    return HttpResponse(text)

def about(request):
    context = f"""<h1>
    Имя: {author['name']} <br>
    Отчество: {author['middle_name']} <br>
    Фамилия: {author['last_name']} <br>
    Телефон: {author['phone']} <br>
    Почта: {author['email']} <br></h1>
    <br>
    <br>
    <a href = "/">Home</a>
    <br>
    <br>
    <a href = "/items">Список товаров</a>
"""

    return HttpResponse(context)

"""По указанному id возвращает элемент из списка"""
def get_item(request, item_id: int):
    for item in items:
        if item["id"] == item_id:
            result = f"""
            <h1> Имя: {item["name"]} </h1>
            <p> Количество: {item["quantity"]} </p>
            <p> <a href='/items'> Назад к списку товаров </a></p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'<strong>Item with id={item_id} not found </strong>')

def get_items(request):
    result = f"""
    <br>
    <br>
    <a href = "/">Home</a>
    <br>
    <br>
    <h1> Список товаров </h1><ol>"""
    for item in items:
        result += f""" <li> <a href='/item/{item["id"]}'> {item["name"]} </a> </li>"""
    result += "</ol>"
    return HttpResponse(result)    
