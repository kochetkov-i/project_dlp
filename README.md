# project_dlp

[![Build Status](https://app.travis-ci.com/kochetkov-i/project_dlp.svg?branch=main)](https://app.travis-ci.com/kochetkov-i/project_dlp)
travis-ci запускает линтер Flake8 с дефолтными параметрами

для запуска локально:
- стартуем локальный сервер postgres
- с помощью миграций создаем/обновляем бд [ flask db upgrade ]
- создаем конфиг файл webapp/config.py 
```py
class Config:
    DEBUG = True
    TESTING = False
    DATABASE_HOST = 'localhost'
    DATABASE_USER = 'b'
    DATABASE_PASSWORD = ''
    DATABASE_PORT = '5432'
    DATABASE_NAME = 'db_moneycollect'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        DATABASE_USER, DATABASE_PASSWORD,
        DATABASE_HOST, DATABASE_PORT,
        DATABASE_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''
    FLASK_APP = 'webapp'
    FLASK_ADMIN_SWATCH = 'cerulean'
    REMEMBER_COOKIE_DURATION = timedelta(days=5)
```
- запускаем приложение [ flask run ]

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
