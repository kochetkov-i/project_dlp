from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, IntegerField
from wtforms.validators import DataRequired


class CheckoutForm(FlaskForm):
    collection_name = StringField(
        'Получатель',
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    collection_id = HiddenField()
    amount = IntegerField(
        'Сумма',
        validators=[DataRequired()],
        render_kw={"class": "form-control"})
    pay = SubmitField(
        'Перевести',
        render_kw={"class": "btn btn-primary"})
