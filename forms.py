from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class AddPlaceForm(FlaskForm):
    name = StringField('Place name', validators=[DataRequired()])
    lant = StringField('Place lant', validators=[DataRequired()])
    long = StringField('Place long', validators=[DataRequired()])
    description = StringField('Place description', validators=[])
    photos = FileField('Plase photos', validators=[])
    submit = SubmitField('Add place')
