from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user)