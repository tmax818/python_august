from flask_app import app, render_template, request, redirect, session, bcrypt, flash
from flask_app.models.user import User


# TODO ROOT ROUTE
@app.route('/')
def index():
    return render_template('index.html')

# TODO REGISTER
@app.route('/register', methods = ['post'])
def register():
    ## validate them
    print(request.form)
    data = {'email': request.form['email']}
    user_in_db = User.get_one_with_email(data)
    if user_in_db:
        flash("email already in use", 'email')
        return redirect('/')
    if not User.validate_user(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    print(hashed_pw)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    print(data)
    ## add user to database
    user_id = User.save(data)
    ## log in the user by adding them to session
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']

    return redirect('/dashboard')

# TODO LOGIN
@app.route('/login', methods = ['post'])
def login():
    ## check the database for the email they enter
    data = {'email': request.form['log_email']}
    user_in_db = User.get_one_with_email(data)
    if not user_in_db:
        flash("invalid credentials")
        return redirect('/')
    ## check the password the supply matches the hash in the database
    if not bcrypt.check_password_hash(user_in_db.password, request.form['log_password']):
        flash("invalid credentials")
        return redirect('/')
    ## log in the use by adding to session
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
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
    data = {'id': session['user_id']}
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/update/user', methods = ['POST'])
def update_user():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/edit/user')
    User.update(request.form)
    return redirect('/dashboard')

@app.route('/show/user')
def show_user():
    data = {'id': session['user_id']}
    return render_template('show_user.html', user = User.get_one_with_recipes(data))


