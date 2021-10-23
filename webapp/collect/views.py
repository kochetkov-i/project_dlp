from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user, login_required
from webapp.collect.forms import EditCollectForm
from webapp import db, basedir
from webapp.config import Config
from webapp.collect.models import Collections, Images
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
import os


blueprint = Blueprint('collect', __name__, url_prefix='/collect')


@blueprint.route('/edit_collect')
@login_required
def edit_collect():
    edit_collect_form = EditCollectForm()
    title = "Редактирование"
    return render_template(
        'collect/edit_collect.html',
        page_title=title,
        form=edit_collect_form,
        current_user=current_user)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS


def upload_file(attach_files, collection_id):
    for file in attach_files:
        filename = secure_filename(file.filename)
        folder = os.path.join(
            basedir,
            Config.UPLOAD_FOLDER,
            str(collection_id)
        )
        full_path = os.path.join(folder, filename)
        link_path = os.path.join(
            Config.UPLOAD_FOLDER,
            str(collection_id),
            filename
        )
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

        file.save(full_path)

        new_image = Images(
            collections_id=collection_id,
            link=link_path,
            upload_date=datetime.now()
        )
        db.session.add(new_image)
        db.session.commit()


@blueprint.route('/procces_edit_collect', methods=['GET', 'POST'])
@login_required
def procces_edit_collect():
    edit_collect_form = EditCollectForm()
    if edit_collect_form.validate_on_submit():
        delta = timedelta(days=edit_collect_form.max_days.data)
        new_collection = Collections(
            collector_user_id=current_user.id,
            collection_name=edit_collect_form.name.data,
            description=edit_collect_form.description.data,
            finish_count=edit_collect_form.collection_amount.data,
            finish_time=datetime.now() + delta,
            created_date=datetime.now(),
            last_modify=datetime.now(),
            is_end=False)

        db.session.add(new_collection)
        db.session.commit()
        db.session.refresh(new_collection)

        attach_files = edit_collect_form.attach.data
        if attach_files:
            upload_file(attach_files, new_collection.id)

        return redirect(url_for('main.index'))

    for field, errors in edit_collect_form.errors.items():
        for error in errors:
            flash('Ошибка в поле {}: {}'.format(
                getattr(edit_collect_form, field).label.text,
                error
            ))
        return redirect(url_for('collect.edit_collect'))
