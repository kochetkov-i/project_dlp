from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Optional, EqualTo
from wtforms.fields.html5 import EmailField, TelField


class LoginForm(FlaskForm):
    email = StringField(
        'E-mail',
        validators=[
            DataRequired(),
            Email(),
            Length(min=1, max=64)],
        render_kw={"class": "form-control"})
    password = PasswordField(
        'Пароль',
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    remember_me = BooleanField(
        'Запомнить меня',
        default=True,
        render_kw={"class": "form-check-input form-check-label"})
    submit = SubmitField(
        'Войти',
        render_kw={"class": "btn btn-primary"})


class SignUpForm(FlaskForm):
    email = EmailField(
        'E-mail',
        validators=[
            DataRequired(),
            Email(),
            Length(min=1, max=64)],
        render_kw={"class": "form-control"})
    name = StringField(
        'Имя пользователя',
        validators=[
            DataRequired(),
            Length(min=1, max=32)],
        render_kw={"class": "form-control"})
    surname = StringField(
        'Фамилия пользователя',
        validators=[
            DataRequired(),
            Length(min=1, max=64)],
        render_kw={"class": "form-control"})
    phone = TelField(
        'Номер телефона',
        validators=[
            Optional(),
            Length(min=1, max=32)],
        render_kw={"class": "form-control"})
    password = PasswordField(
        'Введите пароль',
        validators=[
            DataRequired(),
            EqualTo('confirm', message='Пароли должны совпадать')],
        render_kw={"class": "form-control"})
    confirm = PasswordField(
        'Повторите пароль',
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    sign_up = SubmitField(
        'Регистрация',
        render_kw={"class": "btn btn-primary"})
