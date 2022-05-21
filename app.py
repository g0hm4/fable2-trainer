from flask import Flask, render_template, request
import random

# Create an instance of Flask
app = Flask(__name__)

i = 0

# I/O Handling
def ChangeRuntimeCode(action):

	i = random.randint(0,1000)

	debugfile = open('C:/Users/banny/Documents/fable modding/Fable 2/data/scripts/RuntimeCode.lua', 'w+')
	content = '''myTestTable.newChecksum = {0}
function myTestTable.CodeToRun()
{1}
end

'''.format(i,action)

	debugfile.write(content)
	debugfile.close()


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.form.get('Enable Free Cam') == 'Enable Free Cam':
			ChangeRuntimeCode('Debug.ToggleFreeCam()')
			pass #do something
		elif  request.form.get('action2') == 'VALUE2':
			pass # do something else
		else:
			print ("Failed something")
			pass # unknown
	return render_template('index.html')