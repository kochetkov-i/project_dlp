from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user
from webapp import db
from webapp.contact_us.models import Reporter
from webapp.contact_us.forms import ReporterForm


contact_us = Blueprint('contact_us', __name__)


@contact_us.route('/contact-us')
def contact():
    title = 'Форма обратной связи'
    form = ReporterForm()
    if current_user.is_authenticated:
        form.email.data = current_user.useremail
    return render_template(
        'contact_us/contactus.html',
        title=title,
        form=form
    )


@contact_us.route('/procces_new_contact', methods=['POST'])
def procces_new_contact():
    post_contact = ReporterForm()
    if post_contact.validate_on_submit():
        report = Reporter(
            email=post_contact.email.data,
            username=post_contact.username.data,
            text=post_contact.text.data)
        db.session.add(report)
        db.session.commit()
        flash('Ваше сообщение было отправлено, спасибо')

    return redirect(url_for('main.index'))
