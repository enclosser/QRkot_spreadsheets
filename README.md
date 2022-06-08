# cat_charity_fund

 Сервис для сбора пожертвований для котиков, работающий через API.
 Хранящий информацию о внесенных средствах и проектах для инвестирования
 в базе данных
 
## Запуск проекта

Скопировать проект с репозитория:
```
https://github.com/Andrey-oss-ai/cat_charity_fund.git
```
Установить виртуальное окружение и активировать его
```
python -m venv venv
source venv/bin/activate
```
Обновить менеджер пакетов и установить требуемые зависимости
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Далее в корневой папке проекта создать файл с переменными окружения .env 
```
APP_TITLE = <Название проекта>
DESCRIPTION = <Описание проекта>
DATABASE_URL=<URL путь к базе данных>
FIRST_SUPERUSER_EMAIL = <Логин суперюзера>
FIRST_SUPERUSER_PASSWORD = <Пароль суперюзера>
SECRET=<Секретное слово>
DEBUG = True
SECRET=YOUR_SECRET

TYPE = service_account
PROJECT_ID = watchful-gear-351810
PRIVATE_KEY_ID = <id>
PRIVATE_KEY = <key>
CLIENT_EMAIL = <email>
CLIENT_ID = <client_id>
AUTH_URI = https://accounts.google.com/o/oauth2/auth
TOKEN_URI = https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL = https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL = https://www.googleapis.com/robot/v1/metadata/x509/service-user%40watchful-gear-351810.iam.gserviceaccount.com
EMAIL = <E-mail>
```
Запустить преокт командой
```
uvicorn app.main:app  
```

Документация по проекту и его API функциям будет доступна по адресу

http://127.0.0.1:8000/redoc и http://127.0.0.1:8000/docs

## Автор

Andreu-antonov@yandex.ru