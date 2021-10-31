from flask import Blueprint
from webapp import db
from flask import render_template, redirect
from webapp.contact_us.forms import ContacterForm
from webapp.contact_us.models import Contacter

contact_us = Blueprint('contact_us', __name__)


@contact_us.route('/contactus')
def contact():
    title = 'Форма обратной связи'
    form = ContacterForm()
    return render_template(
        'contact_us/contactus.html',
        title=title,
        form=form
    )
