from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort

from models.user import User
# for decorators
from functools import wraps


def current_user():
    uid = session.get('uid')
    if uid is not None:
        u = User.query.get(uid)
        return u


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        print('admin required')
        if request.args.get('uid') != '1':
            print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        u = current_user()
        if u is None:
            return redirect(url_for('user.login_view'))
        return f(*args, **kwargs)
    return function
