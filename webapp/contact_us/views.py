from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from webapp import db
from webapp.contact_us.models import Reporter
from webapp.auth.models import Users
from webapp.contact_us.forms import ReporterForm


contact_us = Blueprint('contact_us', __name__)


@contact_us.route('/contact-us')
def contact():
    title = 'Форма обратной связи'
    form = ReporterForm()
    return render_template(
        'contact_us/contactus.html',
        title=title,
        form=form
    )


@contact_us.route('/procces_new_contact/<int:id>', methods=['POST'])
def procces_new_contact(id):
    post_contact = ReporterForm()
    if post_contact.validate_on_submit():
        user_email = current_user
        if user_email:
            user_email.useremail = post_contact.email.data
            user_email.username = post_contact.username.data,
        report = Reporter(
            email=post_contact.email.data,
            username=post_contact.username.data,
            text=post_contact.text.data

        )
        db.session.add(report)
        db.session.commit()

    return redirect(url_for('main.index'))
