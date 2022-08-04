from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    title = "All about Tyler"
    return render_template('about.html', title = title)


if __name__ == '__main__':
    app.run(debug=True)