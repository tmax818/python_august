from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/dojo')
def dojo():
    return "<h1>Dojo!</h1>"

@app.route('/say/<variable>')
def say_hi(variable):
    return f"<h1>Hi {variable}</h1>"

@app.route('/repeat/<int:number>/<variable>')
def repeat(variable, number):
    return f"<h1>{variable * number}</h1>"


if __name__ == '__main__':
    app.run(debug=True)