from config import *
import logging as lg
from flask import Flask, render_template

#logging basic configuration
# lg.basicConfig(filename="log.txt",level=lg.DEBUG)

app = Flask(__name__, template_folder='template')
app.config["DEBUG"] = True


@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('home.html')
           
@app.route('/game/',methods=['GET', 'POST'])
def perform_upload():
    return render_template('game.html')







if __name__ == '__main__':
	# when first starting the app from docker, we load the model into memory
	# and then start the flask app
	app.run(debug=False, host=HOST, port=PORT, use_reloader=False)