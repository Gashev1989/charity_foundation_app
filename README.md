# Приложение QRkot_spreadseets
### Описание
QRKot — асинхронное API приложение для Благотворительного фонда поддержки котиков.
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
***
Ключевые возможности приложения:
- Целевые проекты для пожертвований создаются администраторами сайта. 
- Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы.
- Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
- Администратор может получать в свой аккаунт отчет с закрытыми проектами, отсортированными по скорости сбора средств в формате Google Spreadsheets.

### Технологии
**Язык:**  
Python 3.9  
**Библиотеки:**  
FastAPI
Alembic
SQLAlchemy
Pydantic
Uvicorn
Google Drive API
Google Sheets

### Запуск проекта локально
1. Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:Gashev1989/QRkot_spreadsheets.git
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
3. Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
4. В корневой директории проекта создать файл .env, в котором указать:
```
APP_TITLE=QRKOT
APP_DESCRIPTION=Приложение для Благотворительного фонда поддержки котиков QRKot
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db (укажите свой вариант)
SECRET=DEFAULT (укажите своё слово для хэширования паролей)
FIRST_SUPERUSER_EMAIL=admin@example.com (укажите email администратора приложения)
FIRST_SUPERUSER_PASSWORD=admin (придумайте пароль администратора)
```
*Администратор (SUPERUSER) с вышеуказанными данными будет создан автоматически*
Для получения отчетов в аккаунт Google, дополнительно укажите в .env
```
EMAIL= (добавьте свой)
TYPE=service_account
PROJECT_ID= (добавьте свой)
PRIVATE_KEY_ID= (добавьте свой)
PRIVATE_KEY= (добавьте свой)
CLIENT_EMAIL= (добавьте свой)
CLIENT_ID= (добавьте свой)
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL= (добавьте свой)
UNIVERSE_DOMAIN=googleapis.com
```
5. Сделайте миграции командой:
```
alembic upgrade head
```
6. Из корневой директории запустите приложение командой:
```
uvicorn app.main:app
```

### Примеры запросов API и документация
Для просмотра примера запросов и документации API, после локального запуска приложения, перейдите по ссылке:
- документация Swagger (http://127.0.0.1:8000/docs)
- документация ReDoc (http://127.0.0.1:8000/redoc)

### Автор
Гашев Константин