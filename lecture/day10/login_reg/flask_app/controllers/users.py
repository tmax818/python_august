from flask_app import app, render_template, request, redirect, session
from flask_app.models.user import User


# TODO ROOT ROUTE
@app.route('/')
def index():
    return render_template('index.html')

# TODO REGISTER
@app.route('/register', methods = ['post'])
def register():
    ## validate them
    ## add user to database
    ## log in the user by adding them to session
    pass
    return redirect('/dashboard')

# TODO LOGIN
@app.route('/login', methods = ['post'])
def login():
    ## check the database for the email they enter
    ## check the password the supply matches the hash in the database
    ## log in the use by adding to session
    pass
    return redirect('/dashboard')



# TODO LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    pass

# ! OPTIONAL

@app.route('/edit/user')
def edit_user():
    pass

@app.route('/update/user', methods = ['POST'])
def update_user():
    pass

