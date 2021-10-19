from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user
from webapp.collect.forms import EditCollectForm
from webapp import db
from webapp.collect.models import Collections
from datetime import datetime, timedelta


blueprint = Blueprint('collect', __name__, url_prefix='/collect')


@blueprint.route('/edit_collect')
def edit_collect():
    edit_collect_form = EditCollectForm()
    title = "Редактирование"
    return render_template(
        'collect/edit_collect.html',
        page_title=title,
        form=edit_collect_form,
        current_user=current_user)


@blueprint.route('/procces_edit_collect', methods=['POST'])
def procces_edit_collect():
    edit_collect_form = EditCollectForm()
    if not current_user.is_authenticated:
        flash("")
        return redirect(url_for('auth.signup'))
    if edit_collect_form.validate_on_submit():
        delta = timedelta(days=edit_collect_form.max_days.data)
        new_collection = Collections(
            collector_user_id=current_user.id,
            collection_name=edit_collect_form.name.data,
            description=edit_collect_form.description.data,
            finish_count=edit_collect_form.count.data,
            finish_time=datetime.now() + delta,
            created_date=datetime.now(),
            last_modify=datetime.now(),
            is_end=False)

        db.session.add(new_collection)
        db.session.commit()
        return redirect(url_for('main.index'))
    for field, errors in edit_collect_form.errors.items():
        for error in errors:
            flash('Ошибка в поле {}: {}'.format(
                getattr(edit_collect_form, field).label.text,
                error
            ))
        return redirect(url_for('collect.edit_collect'))