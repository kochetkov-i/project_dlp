from flask_admin import AdminIndexView
from flask import redirect, url_for, request
from flask_login import current_user


class WebappModelView(AdminIndexView):

    def is_accessible(self):
        return (current_user.is_authenticated and
                current_user.userrole == 'admin' and
                not current_user.is_deleted)

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))
