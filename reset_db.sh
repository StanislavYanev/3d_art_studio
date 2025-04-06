#!/bin/bash

echo "Изтриване на стара база данни..."
rm -f db.sqlite3

echo "Изтриване на миграции..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

echo "Генериране на нови миграции..."
python manage.py makemigrations

echo "Прилагане на миграциите..."
python manage.py migrate

echo "Готово! Проектът е нулиран успешно."
