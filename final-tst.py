from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home_final.html")

@app.route("/register")
def register():
    return render_template("register_final.html")  

@app.route("/registered", methods=['POST','GET'])
def registered():
    us= request.form["username"]
    pswd=request.form["password"]
    d={'username':str(us),'password':str(pswd)}
    with open("db.txt", "a") as f:
        f.write(str(d)+"\n")
    return "congrats you are successsfully registered." + "<br> "+ "username: "+ us + "<br>" + "password: " + pswd 

@app.route("/login")
def login():
    return render_template("login_final.html")  

@app.route("/login-done", methods=['POST','GET'])
def login_done():
    usr=request.form["username"]
    psw=request.form["password"]
    with open("db.txt","r") as  f:
        contents =f.read()
        contents=contents.split("\n")
        for i in contents:
            return i

if __name__ == '__main__':
    app.run(debug = True)

#for i in f:
#            i=i.split()
 #           for j in i:
  #              return j.strip("{}\",:''") 

    