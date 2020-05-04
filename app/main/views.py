from flask import render_template,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,Comment,Pitch
from .forms import UploadPitch,CommentsForm,UpdateBio
from .. import db


@main.route('/')
def index():
    # upvote=Upvote()
    # downvote=Downvote()
    user=User.query.filter_by(username=current_user.username).first()
    pitch=Pitch.query.filter_by(user_id=user.id).first()
    all_pitch=Pitch.query.all()
    return render_template('index.html',pitches=all_pitch,title='Pitch | Master')

@main.route('/user/<uname>',methods=['GET','POST'])
@login_required
def profile(uname):
    
    user=User.query.filter_by(username=uname).first()
    pitch=Pitch.query.filter_by(user_id=current_user.id).all()
    # pitch=Pitch.query.get(user_id=user.id).all()
    bio=UpdateBio()
    if bio.validate_on_submit():
        user.bio=bio.bio.data
        db.session.add(user)
        db.session.commit()

    image=url_for('static',filename=f'profile/{{current_user.profile_pic_path}}')
    print(image)
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user,image=image,bio=bio,pitches=pitch)

@main.route('/upload/pitch',methods=['GET','POST'])
@login_required
def upload_pitch():
    pitch=UploadPitch()
    if current_user is None:
        abort(404)
    if pitch.validate_on_submit():
        # current_user.pitch_category=pitch.category.data
        # current_user.pitch=pitch.pitch.data
        pitch=Pitch(pitch_category=pitch.category.data,pitch=pitch.pitch.data,user=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Pitch Uploaded')
        return redirect(url_for('main.index'))
    return render_template('profile/update_pitch.html',pitch=pitch,title='Create Pitch')

@main.route('/<int:pname>/comment',methods=['GET','POST'])
@login_required
def comment(pname):
    comments=CommentsForm()
    # user=User.query.filter_by(username=current_user.username).first()
    pitch=Pitch.query.filter_by(id=pname).first()
    comment_query=Comment.query.filter_by(pitch_id=pitch.id).all()
    if comments.validate_on_submit():
        comment=Comment(comment=comments.comment.data,pitch_id=pitch.id,user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment posted!')
        return redirect(url_for('main.index',comments=comment_query))
    
    
    return render_template('profile/comments.html' ,comment=comments)
# def Upvote():
#     counter=0
#     if current_user:
#         vote=counter+1
#         current_user.upvotes=vote
#         db.session.add(current_user)
#         db.session.commit()

#     return counter


# @login_required
# def Downvote():
#     counter=0
#     if current_user:
#         vote=counter+1
#         current_user.downvotes=vote
#         db.session.add(current_user)
#         db.session.commit()

#     return counter