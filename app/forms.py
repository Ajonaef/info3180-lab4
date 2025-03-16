from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired, Regexp


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class UploadForm(FlaskForm):
    file = FileField('Image File', validators=[
        InputRequired(),
        Regexp(r'^[^/\\]\.((jpg|jpeg|png))$', message="Only JPG and PNG files are allowed.")
    ])