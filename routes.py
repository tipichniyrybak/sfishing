from flask import render_template, flash, redirect, request, url_for, json
from __init__ import fl_app
from forms import LoginForm, AddPlaceForm    # RegistrationForm, SendForm
from db_adapter import DB
import os
import datetime
from werkzeug.utils import secure_filename
from ftplib import FTP



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
    rec = DB.query("SELECT * FROM fishing_places")
    add_place_form = AddPlaceForm()
    return render_template('workspace.html', places=rec, form = add_place_form)

@fl_app.route('/get_places', methods=['GET', 'POST'])
def get_places():
    rec = DB.query("SELECT * FROM fishing_places")
    return  json.dumps(rec)

@fl_app.route('/get_place_info', methods=['GET', 'POST'])
def get_place_info():
    place_id = request.args.get('place_id', 0, type=int)

    ftp = FTP()
    ftp.connect('ftpupload.net', 21)
    ftp.login('epiz_24989236', 'FIbPfZKy3F')
    FTP_path = "/htdocs/media/img/places/" + str(place_id)
    ftp.cwd(FTP_path)
    os.chdir(os.path.join(fl_app.root_path, 'static', 'img', 'tmp_places_photo'))

    for filename in ftp.nlst('*.*'):
        fhandle = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, fhandle.write)
        fhandle.close()
    ftp.close()

    rec = DB.query("select * from fishing_places where \"ID\" = " + str(place_id))
    return  json.dumps(rec)


@fl_app.route('/add_place', methods=['POST'])
def add_place():
    sql = "SELECT add_place('" + request.args.get('place_name', '12', type=str) + "', " + str(request.args.get('place_lant', 0.1, type=float)) + ", " + str(request.args.get('place_long', 0.1, type=float)) + ", '" + request.args.get('place_photos', '12', type=str) + "', '" + request.args.get('place_description', '12', type=str) + "')"
    print(sql)
    rec = DB.query(sql)
    if rec[0][0] != 0:

        ftp = FTP()
        ftp.connect('ftpupload.net', 21)
        ftp.login('epiz_24989236', 'FIbPfZKy3F')
        FTP_path = "/htdocs/media/img/places/" + str(rec[0][0])

        if not FTP_path in ftp.nlst():
            ftp.mkd(FTP_path)

        ftp.cwd(FTP_path)

        for photo in request.files.getlist('files[]'):
            filename = secure_filename(photo.filename)
            file_path = os.path.join(fl_app.root_path, 'static', 'img', 'tmp_places_photo', filename)
            photo.save(file_path)
            fp = open(file_path, 'rb')
            ftp.storbinary('STOR %s' % os.path.basename(filename), fp, 1024)
            os.remove(file_path)

        fp.close()

    return json.dumps(rec[0][0])


@fl_app.route('/map')
def map():
    rec = DB.query("SELECT * FROM fishing_places")
    return render_template('map.html', places=rec)

@fl_app.route('/controls')
def controls():
    return render_template('controls.html')
