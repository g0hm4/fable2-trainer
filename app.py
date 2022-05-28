from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime
import random
import fable_dicts


# Create an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] =  'secret'

commandlist = []

with open('inventory_commands.txt') as file:
    inventorycommands = file.readlines()
    inventorycommands = [line.rstrip() for line in inventorycommands]

for item in fable_dicts.fabledicts:
	for subitem in item:
		commandlist.append(subitem)
i = 0

# I/O Handling
def ChangeRuntimeCode(action):

	i = random.randint(0,1000)

	debugfile = open('C:/Users/banny/Documents/fable modding text/Fable 2/data/scripts/RuntimeCode.lua', 'w+')
	content = '''myTestTable.newChecksum = {0}
function myTestTable.CodeToRun()
{1}
end

'''.format(i,action)

	debugfile.write(content)
	debugfile.close()

# Form

class TextForm(FlaskForm):
	csrf = False
	command = StringField("Command", validators=[DataRequired()])
	submit = SubmitField("Submit")

class DropDownForm(FlaskForm):
	csrf = False
	command = SelectField('Command', choices = commandlist, validators = [DataRequired()])
	submit = SubmitField("Submit")

class GiveHeroStuffForm(FlaskForm):
	csrf = False
	command = SelectField('Command', choices = inventorycommands, validators = [DataRequired()])
	submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
	form=TextForm()
	if form.validate_on_submit():
			ChangeRuntimeCode(form.command.data)
			flash("RuntimeCode.lua updated" + ' @ ' + datetime.now().strftime('%H:%M:%S'))

	return render_template('index.html', 
		form=form)

@app.route('/dropdown', methods=['GET', 'POST'])
def dropdown():
	form=DropDownForm()
	if form.validate_on_submit():
			ChangeRuntimeCode(form.command.data)
			flash("RuntimeCode.lua updated" + ' @ ' + datetime.now().strftime('%H:%M:%S'))

	return render_template('index.html', 
		form=form)

@app.route('/giveherostuff', methods=['GET', 'POST'])
def giveherostuff():
	form=GiveHeroStuffForm()
	if form.validate_on_submit():
			ChangeRuntimeCode(form.command.data)
			flash("RuntimeCode.lua updated" + ' @ ' + datetime.now().strftime('%H:%M:%S'))

	return render_template('giveherostuff.html', 
		form=form)