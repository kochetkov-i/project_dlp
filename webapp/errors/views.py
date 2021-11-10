from flask import render_template, Blueprint


blueprint = Blueprint('errors', __name__)


@blueprint.app_errorhandler(404)
def not_found(e):
    return render_template("errors/404.html"), 404


@blueprint.app_errorhandler(400)
def bad_request(e):
    return render_template("errors/400.html"), 400


@blueprint.app_errorhandler(403)
def payment_failed(e):
    return render_template("errors/403.html"), 403
