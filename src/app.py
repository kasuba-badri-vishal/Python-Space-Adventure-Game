from config import *
import logging as lg
from flask import Flask, render_template

#logging basic configuration
# lg.basicConfig(filename="log.txt",level=lg.DEBUG)

app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')
app.config["DEBUG"] = True


@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/about',methods=['GET', 'POST'])
def about_game():
    return render_template('about.html')
           
@app.route('/rules',methods=['GET', 'POST'])
def rules():
    return render_template('rules.html')

@app.route('/stats',methods=['GET', 'POST'])
def game_stats():
    return render_template('stats.html')
           
@app.route('/experience',methods=['GET', 'POST'])
def feedback():
    return render_template('feedback.html')







if __name__ == '__main__':
	# when first starting the app from docker, we load the model into memory
	# and then start the flask app
	app.run(debug=False, host=HOST, port=PORT, use_reloader=False)