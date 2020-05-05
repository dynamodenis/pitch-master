from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileField,FileAllowed
class UploadPitch(FlaskForm):
    # category=StringField('Pitch Category:', validators=[DataRequired(),Length(max=20)])
    category=SelectField('Select Category',validators=[DataRequired()],choices=[('Interview Pitch','Interview Pitch'),
                                                    ('Products Pitch','Products Pitch'),
                                                    ('Tech Pitch','Tech Pitch'),
                                                    ('Political Pitch','Political Pitch'),
                                                    ('Religious Pitch','Religious Pitch'),
                                                    ('Pickup Lines','Pickup Lines'),
                                                    ('Others','None of the above')])
    pitch=TextAreaField('Write Pitch:',validators=[DataRequired()])
    submit=SubmitField('Post Pitch')
  
class CommentsForm(FlaskForm):
    comment=TextAreaField('Type comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')

class UpdateBio(FlaskForm):
    bio=StringField('Create a Bio:')
    picture=FileField('Choose Profile Picture', validators=[FileAllowed(['jpeg','png','jpg'])])
    submit=SubmitField('Update Bio')