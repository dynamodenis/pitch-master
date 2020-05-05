from flask import render_template,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Comment,Pitch
from .forms import UploadPitch,CommentsForm,UpdateBio
from .. import db

def Upvote(pitch):
    counter=0
    if pitch:
        vote=counter+1
        uvotes=Pitch(upvotes=vote)
        db.session.add(uvotes)
        db.session.commit()

    return uvotes



def Downvote(pitch):
    counter=0
    if pitch:
        vote=counter+1
        dvotes=Pitch(downvotes=vote)
        db.session.add(dvotes)
        db.session.commit()

    return dvotes


@main.route('/')
def index():
    # upvote=Upvote()
    # downvote=Downvote()
    # user=User.query.filter_by(username=current_user.username).first()
    # pitch=Pitch.query.filter_by(user_id=user.id).first()
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

    image=url_for('static',filename='profile/{{user.profile_pic_path}}')
    print(image)
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user,image=image,bio=bio,pitches=pitch,title=current_user.username)

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
    return render_template('profile/update_pitch.html',pitch=pitch,title='Create Pitch',legend='Create Pitch')

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
        return redirect(url_for('main.comment',pname=pname))
    
    return render_template('pitch.html' ,comment=comments,pitch=pitch,comments=comment_query,title='Pitch Comment')


@main.route('/<int:pname>/update',methods=['GET','POST'])
@login_required
def update(pname):
    pitches=UploadPitch()
    pitch=Pitch.query.get(pname)
    if pitch.user != current_user:
        abort(403)
    if pitches.validate_on_submit():
        pitch.pitch_category=pitches.category.data
        pitch.pitch=pitches.pitch.data
        db.session.commit()
        flash('Successfully Updated!')
        return redirect(url_for('main.profile',uname=pitch.user.username))
    elif request.method=='GET':
        pitches.category.data=pitch.pitch_category
        pitches.pitch.data=pitch.pitch

    return render_template('profile/update_pitch.html',pitch=pitches,legend="Update Pitch")

@main.route('/<int:pitch_id>/delete',methods=['POST'])
@login_required
def delete_pitch(pitch_id):
    pitch=Pitch.query.get(pitch_id)
    if pitch.user != current_user:
        abort(403)
    
    db.session.delete(pitch)
    db.session.commit()
    flash('Pitch Delete!')
    return redirect(url_for('main.profile',uname=pitch.user.username))