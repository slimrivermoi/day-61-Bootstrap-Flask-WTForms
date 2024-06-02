from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4


class MyForm(FlaskForm):
    #validators ensure email is a required field and has message for missing symbol.
    email = EmailField(label='Email',
                       validators=[DataRequired(), Email(message="Email is missing @ or .")],
                       render_kw={'style': 'width: 30ch'}
                       )
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")
    cancel = SubmitField(label="Cancel")


app = Flask(__name__)

## Set the secret key to some random bytes.
app.secret_key = b'\xa4#\x86\xd3w\xd0\xfdwv\xeeKS+*\xb0`"ka\x88\x08\xc2\x838'

## initializing Bootstrap Flask for the app --> this is to add in Bootstrap Flask styling
bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    ## This validation was successful after user submitted the form
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
