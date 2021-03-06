# project_dlp

[![Build Status](https://app.travis-ci.com/kochetkov-i/project_dlp.svg?branch=main)](https://app.travis-ci.com/kochetkov-i/project_dlp)

travis-ci запускает линтер Flake8 с отключенными проверками E402,W503

MAC friendly инструкция для запуска локально:
- скачиваем проект
- стартуем локальный сервер postgres
```Запуск вручную
pg_ctl -D /usr/local/var/postgres start
Остановить вручную
pg_ctl -D /usr/local/var/postgres stop
Запуск автоматически
"To есть launchd запустить postgresql сейчас и перезапустить при входе в систему:"
brew services start postgresql
```
- создаем пользователя в БД
```
CREATE DATABASE <DATABASE_NAME> OWNER "<YOUR_OWNER>";
CREATE ROLE <USER_NAME> WITH LOGIN PASSWORD 'password' CONNECTION LIMIT -1;
```

- создаем конфиг файл webapp/config.py 
```py
class Config:
    DEBUG = True
    TESTING = False
    DATABASE_HOST = 'localhost'
    DATABASE_USER = '<USER_NAME>'
    DATABASE_PASSWORD = ''
    DATABASE_PORT = '5432'
    DATABASE_NAME = '<DATABASE_NAME>'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        DATABASE_USER, DATABASE_PASSWORD,
        DATABASE_HOST, DATABASE_PORT,
        DATABASE_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '<SECRET_KEY>'
    FLASK_APP = 'webapp'
    FLASK_ADMIN_SWATCH = 'cerulean'
    REMEMBER_COOKIE_DURATION = timedelta(days=5)
    UPLOAD_FOLDER = 'images/'
    ALLOWED_EXTENSIONS = set(['jpg', 'png'])
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
```
- создаем env и устанавливаем зависимости
```
python3 -m venv env

source env/bin/activate

/<your path>/env/bin/python3 -m pip install --upgrade pip

pip install -r ./webapp/requirements.txt
```
- с помощью миграций создаем/обновляем бд
```
export FLASK_APP=webapp && flask db upgrade
```
- запускаем приложение 
```
./run.sh
```
- создаем администратора скриптом
```
create_admin.py
```

## Веб приложение: сайт для размещелния сбора средств (краундфандинг)
### Цель проекта: Разработать сайт для сбора средств. Дать пользователям возможность регистрироваться и создавать объявления по сбору.

### Ключевые возможности:
1. Сделать на сайте просмотр списка объявлений и просмотр страницы объявления
2. Сделать регистрацию пользователей
3. Дать пользователю возможность размещать объявления, редактировать свои объявления и просматривать список своих объявлений
    * для объявления сделать параметры окончания сбора по времени или сумме
5. Дать возможность выводить средства со своих объявлений
    * обеспечить сбор комиссии
7. Дать возможность переводить средства на любые объявления

#### Дополнения: 
1. Сделать настраиваемую коммисию для вывода средств
2. Сделать выделение объявлений
3. Реализовать функционал поиска и фильтрации в списке объявлений
