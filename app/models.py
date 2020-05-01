from . import  db
from datetime import datetime

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(100))
    password_hash=db.Column(db.String)
    bio=db.Column(db.String)
    pitch=db.Column(db.String)
    comments=db.relationship('Comment',backref='user',lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'



class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String)
    pitch=db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch):
        comment=Comment.query.filter_by(pitch=pitch)
        return comment
