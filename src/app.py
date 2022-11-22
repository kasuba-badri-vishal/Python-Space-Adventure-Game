from config import HOST, PORT
from utils import get_stats
from flask import Flask, render_template


### Initializing Flask Application with the required information and details of the location of html files and static data file paths
app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')
app.config["DEBUG"] = True

### Functions of GET requests to fetch the informat of different HTML pages
@app.route('/',methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about_game():
    return render_template('about.html')
           
@app.route('/rules',methods=['GET'])
def rules():
    return render_template('rules.html')

@app.route('/stats',methods=['GET'])
def game_stats():
    return render_template('stats.html')
           
@app.route('/experience',methods=['GET'])
def feedback():
    return render_template('experience.html')




if __name__ == '__main__':
    # Before UI is shown, the stats of the Game are updated
    get_stats()

    # when first starting the app from docker, we load the model into memory
	# and then start the flask app
    app.run(debug=False, host=HOST, port=PORT, use_reloader=False)