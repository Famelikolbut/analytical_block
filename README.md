# Инструкция для запуска проекта

1. Клонирование репозитория

```
git clone <URL репозитория>
cd <название репозитория>
```

2. Создание виртуального окружения и установка зависимостей

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Запуск Docker Compose

```
docker-compose up -d --build
```

4. Миграция базы данных и создание суперпользователя

```
docker exec -it my_web_app bash
python manage.py migrate
python manage.py createsuperuser
```

5. Запуск тестов

```
docker exec my_web_app python manage.py test
```