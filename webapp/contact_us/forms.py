from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length


class ReporterForm(FlaskForm):
    email = StringField(
        'Ваш email',
        validators=[
            DataRequired(),
            Length(min=1, max=32)],
        render_kw={'class': 'form-control'})

    username = StringField(
        'Ваше имя',
        validators=[
            DataRequired(),
            Length(min=1, max=32)],
        render_kw={'class': 'form-control'})

    text = TextAreaField(
        'Сообщение',
        validators=[
            DataRequired(),
            Length(min=1, max=300)],
        render_kw={'class': 'form-control'})

    submit = SubmitField(
        'Отправить',
        render_kw={'class': 'btn btn-primary'})
