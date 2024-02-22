from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    user_id = StringField('Id астронавта', validators=[DataRequired()])
    password_1 = PasswordField('Пароль', validators=[DataRequired()])
    cap_id = StringField('Id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route("/login", method=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/succes")


@app.route("/")
def index():
    return redirect("/login")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
