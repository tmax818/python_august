from flask import Flask, render_template
import requests
from pprint import pprint
app = Flask(__name__)
global url 
@app.route('/')
def index():
    url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01"
    return render_template('index.html', data = requests.get(url,headers = {'token': 'hxaHeQczjNjFqNJtWyCxxajuNFrTqDlc'}).json())

@app.route('/character')
def characters():
    loc_url = "https://rickandmortyapi.com/api/character"
    data = requests.get(loc_url).json()
    pprint(data)
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)