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
    d={}
    d[us]=pswd
    with open("db.txt", "a") as f:
        for key in d:
            s= key + " "+ d[key]
            f.write(s+"\n")
    return "congrats you are successsfully registered." + "<br> "+ "username: "+ us + "<br>" + "password: " + pswd 

@app.route("/login")
def login():
    return render_template("login_final.html")  

@app.route("/login-done", methods=['POST','GET'])
def login_done():
    usr=request.form["username"]
    psw=request.form["password"]
    with open("db.txt","r") as  f:
        for i in f:
            data =i.split()
            if data[0] == usr and data[1] == psw:
                flag= True
                break
            else:
                flag=False                
    if flag == True:
        return "Success.. Welcome " + data[0] 
    else:
        return "failed to login... Check your credentials"

if __name__ == '__main__':
    app.run(debug = True)



    