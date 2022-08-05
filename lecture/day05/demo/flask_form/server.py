from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)   
app.secret_key = "any string I want..."

@app.route('/')        
def hello_world():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def handle_form_data():
    print(request.form)
    session['key'] = request.form['key']

    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":     
    app.run(debug=True)   