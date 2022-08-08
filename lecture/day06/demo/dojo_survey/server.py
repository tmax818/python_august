from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "any string I want, this is the key for the incripted cookie"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/survey', methods=["POST"])
def create_survey():
    print(request.form)
    session['name'] = request.form['ninja_name']
    session['location'] = request.form['location']
    print(session)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')




if __name__ == "__main__":
    app.run(debug=True)