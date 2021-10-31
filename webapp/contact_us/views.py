from flask import Blueprint
from flask import render_template
from webapp.contact_us.forms import ContacterForm

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
