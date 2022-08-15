from flask_app import app, render_template, request, redirect
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/new/recipe')
def new_recipe():

    return render_template('new_recipe.html')


# ! CREATE 
@app.route('/create/recipe', methods = ['post'])
def create_recipe():
    print(request.form)
    recipe = Recipe.save(request.form)
    return redirect('/recipes')

# ! READ ALL
@app.route('/dashboard')
@app.route('/recipes')
def recipes():
    return render_template('dashboard.html', recipes = Recipe.get_all())

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
    Recipe.update(request.form)
    return redirect(f"/show/{request.form['id']}")

# ! DELETE 
@app.route('/delete/<int:id>')
def delete_recipe(id):
    Recipe.destroy({'id': id})
    return redirect(f"/")