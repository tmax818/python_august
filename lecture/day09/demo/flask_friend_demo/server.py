from flask import Flask, render_template
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends = friends)
    
@app.route("/show/<int:id>")
def show(id):
    data = {'id': id}
    # call the get all classmethod to get all friends
    friend = Friend.get_one(data)
    print(friend)
    return render_template("show_friend.html", friend = friend)
            
if __name__ == "__main__":
    app.run(debug=True)