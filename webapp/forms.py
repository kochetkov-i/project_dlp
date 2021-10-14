from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Optional


class WithdrawalMoneyForm(FlaskForm):
    name = StringField(
        'Название',
        validators=[
            DataRequired(),
            Length(min=1, max=256)],
        render_kw={"class": "form-control"})
    description = TextAreaField(
        'Описание',
        validators=[
            DataRequired(),
            Length(min=1, max=2048)],
        render_kw={"class": "form-control"})
    attach = FileField(
        'Приложение',
        validators=[Optional()],
        render_kw={"class": "form-control"})
    edit = SubmitField(
        'Редактировать',
        render_kw={"class": "btn btn-primary"})
    submit = SubmitField(
        'Сохранить',
        render_kw={"class": "btn btn-primary"})
