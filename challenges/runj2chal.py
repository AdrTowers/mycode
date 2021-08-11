#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key = "Babu Frik"

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]
# pull in the value of score as an int
@app.route("/", methods= ["GET", "POST"])
def input_host():
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    if "username" in session and session["username"] == "admin":
        if request.method == "POST":
            hostname = request.form.get("hostname")
            ip = request.form.get("ip")
            fqdn = request.form.get("fqdn")
            groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
    return render_template("hostname.html", groups= groups)

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        session["username"] = request.form.get("username")
    if "username" in session and session["username"] == "admin":
        return render_template("newform.html")
    else:
        return """
    <form action= "" method = "POST">
        <p>Invalid Login.</p>
        <p><input type= text name= username></p>
        <p><input type=submit value= Login></p>
    </form>
    """

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

