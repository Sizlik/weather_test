# README.md

## FAQ
Тестовое задание.

### Tech stack:
- Django REST
- PyTelegramBotApi
- Requests
- Docker
- Docker Compose
- Yandex API GeoCode, Погода

## Запуск проекта:
1. Copy .env.example -> .env
2. Заменить YOUR_API_KEY на ваш API_KEY, если нужно заменить endpoint.
3. docker-compose up -d

## Запуск проекта локально:

0. Создать виртуальное окружение

### Бот

1. 
```bash
cd bot
```

2.
```bash
pip install -r requirements.txt
```

3.
```bash
python bot.py
```

### Django project

1. 
```bash
cd api
```
2. 
```bash
pip install -r requirements.txt
```

3. 
```bash
python manage.py runserver
```
