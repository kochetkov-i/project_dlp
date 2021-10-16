from flask import render_template, Blueprint
from flask_login import current_user
from webapp.collect.forms import EditCollectForm


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
