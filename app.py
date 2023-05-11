# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Shruthi Devendiran" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/dad")
def dad():
    name = "Devendiran"
    age="48"

    return render_template("father.html", name=name , age=age)

# define the route to mother webpage
@app.route("/mom")
def mom():
    name="Mythili Devendiran"
    age = "42"

    return render_template("mother.html",name=name, age=age)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name="Shriddi.S"
    age = "12"

    return render_template("friend.html", name=name, age=age)

# add other routes, if you want
@app.route("/sis")
def sister():
    name = "Keerthi Devendiran"
    age = "20"
    
    return render_template("index.html", name=name, age=age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
