from flask import render_template
from . import auth
from .forms import LoginForm,RegistrationForm
from .. import db

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    return render_template('auth/login.html',form=form)

@auth.route('/register', methods=['GET','POST'])
def register():
    register=RegistrationForm()
    return render_template('auth/register.html',register=register)
