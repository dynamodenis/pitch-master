from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,InputRequired
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    username=StringField('Type Your Username:',validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Enter Your Email Address:', validators=[Email(),DataRequired()])
    password=PasswordField('Enter Password:',validators=[DataRequired(),EqualTo('password_confirm',message='Passwords Must Match')])
    password_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Create Account')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('This email is taken')

    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('This username is taken')

class LoginForm(FlaskForm):
    email=StringField('Enter Your Email Address:', validators=[Email(),DataRequired()])
    password=PasswordField('Enter Password:',validators=[InputRequired()])
    remember=BooleanField('Remember me:')
    submit=SubmitField('Login')
 