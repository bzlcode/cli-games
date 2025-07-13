from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home_login.html")
@app.route("/login", methods=['GET','POST'])
def login():
    u_name = request.form["username"]
    pswd =request.form["password"]
    return "The username is : "+ u_name + " and password is: "+ pswd

if __name__ == "__main__":
    app.run(debug=True)