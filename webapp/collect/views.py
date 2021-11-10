from flask import render_template, redirect, url_for, flash, Blueprint, abort
from flask_login import current_user, login_required
from webapp.collect.forms import EditCollectForm
from webapp import db, basedir
from webapp.config import Config
from webapp.collect.models import Collections, Images
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
import os


blueprint = Blueprint('collect', __name__, url_prefix='/collect')


@blueprint.route('/view_collect/<int:id>')
def view_collect(id):
    collection = Collections.query.filter_by(id=id).first()
    if collection:
        title = "Просмотр"
        return render_template(
            'collect/view_collect.html',
            page_title=title,
            current_user=current_user,
            collection=collection)
    abort(404)


@blueprint.route('/edit_collect/<int:id>')
@login_required
def edit_collect(id):
    edit_collect_form = EditCollectForm()
    collection = Collections.query.filter_by(id=id).first()
    if collection:
        edit_collect_form.name.data = collection.collection_name
        edit_collect_form.description.data = collection.description
        edit_collect_form.collection_amount.data = collection.finish_count
        edit_collect_form.max_days.data = (
            collection.finish_time - collection.created_date).days

        title = "Редактирование"
        return render_template(
            'collect/edit_collect.html',
            page_title=title,
            form=edit_collect_form,
            current_user=current_user,
            collection=collection)

    abort(404)


@blueprint.route('/new_collect')
@login_required
def new_collect():
    edit_collect_form = EditCollectForm()
    title = "Создать новый сбор"
    return render_template(
        'collect/new_collect.html',
        page_title=title,
        form=edit_collect_form,
        current_user=current_user)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS


def upload_file(attach_files, collection_id):
    for file in attach_files:
        if file.filename and allowed_file(file.filename):
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
        else:
            flash('Can not upload files')


@blueprint.route('/procces_edit_collect/<int:id>', methods=['POST'])
@login_required
def procces_edit_collect(id):
    edit_collect_form = EditCollectForm()
    delta = timedelta(days=edit_collect_form.max_days.data)
    if edit_collect_form.validate_on_submit():
        collection = Collections.query.filter_by(id=id).first()
        if collection:
            collection.last_modify = datetime.now()
            collection.collection_name = edit_collect_form.name.data
            collection.description = edit_collect_form.description.data
            collection.finish_count = edit_collect_form.collection_amount.data
            collection.finish_time = datetime.now() + delta

            db.session.add(collection)
            db.session.commit()
            db.session.refresh(collection)

            attach_files = edit_collect_form.attach.data
            if len(attach_files):
                upload_file(attach_files, collection.id)

            return redirect(url_for('main.index'))

        abort(404)

    for field, errors in edit_collect_form.errors.items():
        for error in errors:
            flash('Ошибка в поле {}: {}'.format(
                getattr(edit_collect_form, field).label.text,
                error
            ))
        return redirect(url_for('collect.edit_collect'))


def check_collect():
    today = datetime.now()
    time_money = Collections.query.order_by(is_end=False)
    if time_money.amount == time_money.finish_amount:
        stop_collect = Collections(
            is_end=True
        )

        db.session.add(stop_collect)
        db.session.commit()
        db.session.refresh(stop_collect)

    if today >= time_money.finish_time:
        stop_collect = Collections(
            is_end=True
        )

        db.session.add(stop_collect)
        db.session.commit()
        db.session.refresh(stop_collect)


@blueprint.route('/procces_new_collect', methods=['POST'])
@login_required
def procces_new_collect():
    edit_collect_form = EditCollectForm()
    delta = timedelta(days=edit_collect_form.max_days.data)
    if edit_collect_form.validate_on_submit():
        collection = Collections(
            collector_user_id=current_user.id,
            collection_name=edit_collect_form.name.data,
            description=edit_collect_form.description.data,
            finish_count=edit_collect_form.collection_amount.data,
            finish_time=datetime.now() + delta,
            last_modify=datetime.now(),
            created_date=datetime.now(),
            is_end=False)

        db.session.add(collection)
        db.session.commit()
        db.session.refresh(collection)

        attach_files = edit_collect_form.attach.data
        if len(attach_files):
            upload_file(attach_files, collection.id)

        return redirect(url_for('main.index'))

    for field, errors in edit_collect_form.errors.items():
        for error in errors:
            flash('Ошибка в поле {}: {}'.format(
                getattr(edit_collect_form, field).label.text,
                error
            ))
        return redirect(url_for('collect.new_collect'))
