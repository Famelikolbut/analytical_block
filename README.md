<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Инструкция для запуска проекта</title>
</head>
<body>

<h1>Инструкция для запуска проекта</h1>

<h2>1. Клонирование репозитория</h2>
<pre><code>git clone &lt;URL репозитория&gt;
cd &lt;название репозитория&gt;</code></pre>

<h2>2. Создание виртуального окружения и установка зависимостей</h2>
<pre><code>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt</code></pre>

<h2>3. Запуск Docker Compose</h2>
<pre><code>docker-compose up -d --build</code></pre>

<h2>4. Миграция базы данных и создание суперпользователя</h2>
<pre><code>docker exec -it analytical_block-web-1 bash
python manage.py migrate
python manage.py createsuperuser</code></pre>

<h2>5. Запуск тестов</h2>
<pre><code>docker exec analytical_block-web-1 python manage.py test</code></pre>

</body>
</html>