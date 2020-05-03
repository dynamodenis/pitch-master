from flask import render_template,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User
from .forms import UploadPitch
from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    image=url_for('static',filename=f'profile/{{current_user.profile_pic_path}}')
    print(image)
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user,image=image)

@main.route('/upload/pitch',methods=['GET','POST'])
@login_required
def upload_pitch():
    pitch=UploadPitch()
    if current_user is None:
        abort(404)
    if pitch.validate_on_submit():
        current_user.pitch_category=pitch.category.data
        current_user.pitch=pitch.pitch.data
        db.session.add(current_user)
        db.session.commit()
        flash('Pitch Uploaded')
        return redirect(url_for('main.index',user=current_user))
    return render_template('profile/update_pitch.html',pitch=pitch,title='Create Pitch')