##QRkot_spreadseets

###Благотворительный фонд поддержки котиков.
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

###Стек технологий:
- Python 3.9
- FastAPI
- SQLAlchemy
- Google Sheets API
- Google Drive API

#### Установка проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/agamova/QRkot_spreadsheets.git
```

```
cd QRkot_spreadsheets
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В корневой директории проекта создать файл .env с переменными:

```
FPP_TITLE=EXAMPLE_TITLE
APP_DESCRIPTION=EXAMPLE_DESCRIPTION
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=YOUR_SECRET
TYPE=service_account
PROJECT_ID=EXAMPLE_ID
PRIVATE_KEY_ID=YOUR_PRIVATE_KEY_ID
PRIVATE_KEY=YOUR_PRIVATE_KEY
CLIENT_EMAIL=EXAMPLE_CLIENT_EMAIL
CLIENT_ID=YOUR_CLIENT_ID
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=YOUR_CLIENT_X509_CERT_URL
EMAIL=your@email
```

Запустите проект командой:

```
 uvicorn app.main:app --reload

```
Проект доступен по адресу:

```
http://127.0.0.1:8000/ 
```

Документация API доступна по адресу:

```
http://127.0.0.1:8000/docs 
```