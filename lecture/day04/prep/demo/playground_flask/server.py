from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/play/<int:number>')
@app.route('/play')
def blue_box(number = 3):
    return render_template('index.html',number = number)

@app.route('/play/<int:number>/<color>')
def repeat(color,number):
    return render_template('index.html',number = number,color = color)

if __name__ == '__main__':
    app.run(debug=True)