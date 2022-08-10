from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users
    return render_template("index.html", users = User.get_all())

@app.route('/users/new')
def new_user():
    return render_template("new.html")

@app.route('/create/user', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

@app.route('/users/<int:id>')
def show_user(id):
    data = {'id': id}
    return render_template('show.html', user = User.get_one(data))

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {'id': id}
    return render_template('edit.html', user = User.get_one(data))

@app.route('/users/update', methods=["POST"])
def update_user():
    print(request.form)
    return redirect('/')




            
if __name__ == "__main__":
    app.run(debug=True)

