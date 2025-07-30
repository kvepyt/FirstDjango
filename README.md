# FirstDjango 200725

# Инструкция по развертыванию проекта
# 1-Создаем директорию для нового проекта Django:
mkdir FirstDjango
cd FirstDjango

# 2-Создаем виртуальное окружение:
python3 -m venv django_venv

# 3-Активируем виртуальное окружение:
source django_venv/bin/activate

# Примечание: для выхода из виртуального окружения venv наберите:
deactivate

# 4-Устанавливаем Django в текущее виртуальное окружение:
(django_venv)$ pip install django
Successfully installed django-<last-version>

#	Запустите интерпретатор python:
python
# >>> import django
# >>> django.VERSION
# должно отобразиться: (3, 1, 0, 'final', 0)
# Примечание: Ctrl+D - для выхода из режима интерпретатора

# 5-Для создания нового проекта:
django-admin startproject FirstDjango .    

# 6-Для запуска проекта:
python3 manage.py runserver
# Перейдите по адресу:  http://127.0.0.1:8000/ в браузере

# 7-Для создания нового приложения в текущем проекте:
python3 manage.py startapp MainApp

## Запуск `ipython` в контексте `django` приложений
```
python manage.py shell_plus --ipython
```

## Выгрузка и загрузка данных при работе с БД
### Выгрузка данных из БД
```
python manage.py dumpdata MainApp --indent 4 > MainApp/fixtures/all_items.json
```
### Загрузка данных в БД
```
python manage.py loaddata MainApp/fixtures/all_items.json
```


## Дополнительно
1. Полезное расширение для шаблонов: `django`
```
ext install batisteo.vscode-django
```
2. Добавить в `settings.json`:
```
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "files.associations": {
        "*.html": "django-html"
    }
```
