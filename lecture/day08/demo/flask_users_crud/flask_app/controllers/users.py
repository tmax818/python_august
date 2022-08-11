from flask_app import app, render_template, request, redirect
from flask_app.models.user import User


# ! CREATE 
@app.route('/create/user', methods = ['post'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

# ! READ ALL
@app.route('/')
def index():
    return render_template('index.html', users = User.get_all())
