from flask import Flask, render_template
import requests
from pprint import pprint
app = Flask(__name__)
global url 
url = "https://rickandmortyapi.com/api"

@app.route('/')
def index():
    return render_template('index.html', data = requests.get(url).json())

@app.route('/character')
def characters():
    loc_url = "https://rickandmortyapi.com/api/character"
    data = requests.get(loc_url).json()
    pprint(data)
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)