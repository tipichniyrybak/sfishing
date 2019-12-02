from flask import render_template, flash, redirect, request, url_for
from __init__ import fl_app
from forms import LoginForm    # RegistrationForm, SendForm
from db_adapter import DB
import os
import datetime

@fl_app.route('/')
@fl_app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@fl_app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        rec = DB.query("select login_user('" + login_form.username.data + "', '" + login_form.password.data + "')")
        if rec[0][0] == -2:
            print('No such user!')
        elif rec[0][0] == -1:
            print('Invalid password')
        else:
            print('Login ok!')
            rec = DB.query("select \"ID\" from users where \"Login\" = " + "'" + login_form.username.data +"'")
            # globals.user_id = rec[0][0]
            # print(globals.user_id)
            return redirect('/workspace')
    return render_template('login.html', title='Sign In', form=login_form)

@fl_app.route('/workspace', methods=['GET', 'POST'])
def workspace():
    return render_template('workspace.html')