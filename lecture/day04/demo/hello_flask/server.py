from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')   # The "@" decorator associates this route with the function immediately following
def hello_world():
    big_secret = "hi mom"
    return render_template('index.html', big_secret = big_secret)  # Return the string 'Hello World!' as a response

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/show/<word>/<int:num>')
def show(word, num):
    return render_template('show.html', x = word, num = num)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

