from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class UploadPitch(FlaskForm):
    category=StringField('Pitch Category:', validators=[DataRequired(),Length(max=20)])
    pitch=TextAreaField('Write Pitch:',validators=[DataRequired()])
    submit=SubmitField('Post Pitch')
  
class CommentsForm(FlaskForm):
    comment=TextAreaField('Type comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')