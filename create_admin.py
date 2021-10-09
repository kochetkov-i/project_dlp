from getpass import getpass
import sys

from webapp import create_app
from webapp.models import Users, db

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя: ')

    if Users.query.filter(Users.username == username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        sys.exit(0)

    new_user = Users(
        username=username,
        userrole="admin")

    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))
