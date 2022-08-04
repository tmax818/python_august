from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    title = "Tyler's amazing flask app"
    return render_template('index.html', title_from_backend = title)  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def route():
    return 'dojo'  # Return the string 'Hello World!' as a response

@app.route('/say/<pineapple>')
def say(pineapple):
    return f"hello {pineapple}"

@app.route('/repeat/<int:num>/<pineapple>')
def repeat(num, pineapple):
    return f"hello {pineapple * num}"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
