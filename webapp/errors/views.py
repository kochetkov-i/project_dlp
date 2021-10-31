from flask import render_template, Blueprint


blueprint = Blueprint('errors', __name__)


@blueprint.app_errorhandler(404)
def not_found(e):
    return render_template("errors/404.html"), 404