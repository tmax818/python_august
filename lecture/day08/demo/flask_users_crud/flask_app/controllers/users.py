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

# ! READ ONE
@app.route('/show/<int:id>')
def show_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

# ! DELETE 
@app.route('/delete/<int:id>')
def delete_user(id):
    User.destroy({'id': id})
    return redirect(f"/")