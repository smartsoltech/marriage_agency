# Указываем базовый образ Python
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update && apt-get install -y netcat-openbsd && \
    python3 -m pip install --upgrade pip && \ 
    python3 -m pip install -r requirements.txt
COPY . .
# Добавляем утилиту ожидания базы данных
COPY wait-for-it.sh .

# Выполняем миграции, когда база данных будет готова
# RUN ./wait-for-it.sh postgres_db:5432 -- python3 ./marriage_agency/manage.py migrate

# Запускаем Django сервер
CMD ["python3", "./marriage_agency/manage.py", "runserver", "0.0.0.0:8000"]
