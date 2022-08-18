from flask import Flask, render_template
import requests
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://rickandmortyapi.com/api"
    data = requests.get(url)
    print(data.json())
    return render_template('index.html')

@app.route('/characters')
def characters():
    url = "https://rickandmortyapi.com/api/character"
    data = requests.get(url)
    pprint(data.json())
    return render_template('index.html', data = data.json())

if __name__ == "__main__":
    app.run(debug=True)