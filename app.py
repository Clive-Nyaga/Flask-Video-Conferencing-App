from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

class RegistrationForm(FlaskForm):    
    email = EmailField('Email', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    # submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # submit = SubmitField('Login')

@app.route('/')
def home():
    return ("Hello, World!")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)

