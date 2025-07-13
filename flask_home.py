from flask import Flask , render_template, redirect, url_for
app = Flask( __name__ )

@app.route ("/")
def home():
    return render_template("homepage.html" ,content="Welcome")

@app.route("/login")
def name_tst():
    return render_template("My_login.html")

@app. route ("/login=success")
def home_login():
    return render_template("homepage.html", content="Welcome You are logged in")

@app. route ("/<name>")
def name(name):
    return render_template("homepage.html",content="Hello " + name)

@app. route ("/calc")
def calc():
    return render_template("calc_og.html")

@app. route ("/cards")
def cards():
    return render_template("divs_tst.html")

if __name__ == "__main__":
    app.run(debug=True)