from flask import Flask, render_template, redirect, url_for, request, g
from flask_bootstrap import Bootstrap

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "changemeondeployment"

Bootstrap(app)

class MyForm(Form):
    name = StringField('Username', validators=[DataRequired()])

@app.route("/", methods=('GET', 'POST'))
def index():
	form = MyForm()
	if form.validate_on_submit():
		return redirect('/success')
	return render_template("login.html", form=form)

@app.route("/success")
def welcome():
	return "welcome!"
		

if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0')
