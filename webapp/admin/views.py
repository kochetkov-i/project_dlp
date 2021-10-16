from webapp.decorators import admin_required
from flask import render_template
from flask import Blueprint


blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/admin')
@admin_required
def admin_index():
    return render_template('admin/index.html')