#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import make_response

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def trivia_question():
   return render_template("trivia.html")

@app.route("/login", methods = ["POST"])
def ans_quest():
    if request.json:
        joke = request.json
        if joke['userans'] == "slap":
            return redirect("/correct")    
        else:
            return redirect("/")

    if request.form.get("userans"):
        userans = request.form.get("userans")
        if userans == "slap":
            #resp now contains the response we normally wpuld have returned
            resp = make_response(redirect("/correct"))
            resp.set_cookie("slappy", userans)
            return resp
        else:
            return redirect("/")
    else:
        return "wakka wakka"

@app.route("/correct")
def correct_ans():
    request.cookies.get("slappy")
    if request.cookies.get("slappy") == "slap":
        return "that is correct"
    else:
        return "You have yet to answer the question correctly"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
