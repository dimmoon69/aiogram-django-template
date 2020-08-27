Предварительные настройки
---
- Создать файл local_settings.py с настройками:

```python
SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'название базы',
        'USER': 'имя пользователь',
        'PASSWORD': 'пароль пользователя',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### Настройки бота
BOT_TOKEN = 'полученный токен от BotFather'
ADMIN_ID = посмотреть id можно с помощью @ShowJsonBot
IP = "localhost"
```
- Создать файл prod_settings.py:

Запуск бота
---
```python
python manage.py bot
```