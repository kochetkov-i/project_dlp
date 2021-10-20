from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange


class EditCollectForm(FlaskForm):
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
    collection_amount = IntegerField(
        'Сумма сбора от 1 до 500000',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=500000)],
        render_kw={"class": "form-control"})
    max_days = IntegerField(
        'Количество дней сбора от 1 до 365',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=365)],
        render_kw={"class": "form-control"})
    attach = FileField(
        'Приложение',
        validators=[
            FileAllowed(['jpg', 'png'], 'Images only!')],
        render_kw={"class": "form-control"})
    submit = SubmitField(
        'Сохранить',
        render_kw={"class": "btn btn-primary"})
