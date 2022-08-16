from flask_app import app, render_template, request, redirect, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/new/recipe')
def new_recipe():

    return render_template('new_recipe.html')


# ! CREATE 
@app.route('/create/recipe', methods = ['post'])
def create_recipe():
    print(request.form )
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    recipe = Recipe.save(request.form)
    return redirect('/recipes')

# ! READ ALL
@app.route('/dashboard')
@app.route('/recipes')
def recipes():
    # ! code to keep non-logged-in users from visiting route
    if 'user_id' not in session:
        return redirect('/logout')

    return render_template('dashboard.html', recipes = Recipe.get_all_with_user())

# ! READ ONE
@app.route('/show/recipe/<int:id>')
def show_recipe(id):
    data = {'id': id}
    recipe = Recipe.get_one(data)
    user = User.get_one({'id':recipe.user_id})
    return render_template('show_recipe.html', recipe = recipe)

# ! UPDATE
@app.route('/edit/<int:id>')
def edit_recipe(id):
    data = {'id':id}
    return render_template('edit_recipe.html', recipe = Recipe.get_one(data))

@app.route('/update/recipe', methods = ['post'])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit/{request.form['id']}")
    Recipe.update(request.form)
    return redirect(f"/dashboard")

# ! DELETE 
@app.route('/delete/<int:id>')
def delete_recipe(id):
    Recipe.destroy({'id': id})
    return redirect(f"/")