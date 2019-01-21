from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from track_and_trace.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Pleae choose another user name.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose another email.")

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CodesForm(FlaskForm):
    input_code = TextAreaField('Enter 2D code value from package', validators=[DataRequired()])
    submit = SubmitField('Enter code')    

class ProductForm(FlaskForm):
    product_name = TextAreaField('Enter product name', validators=[DataRequired()])
    product_batch = TextAreaField('Enter product batch', validators=[DataRequired()])
    expire_date = TextAreaField('Enter product expire', validators=[DataRequired()])
    submit = SubmitField('Enter code')