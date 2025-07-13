from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("project_calc.html")

@app.route("/calc",methods=['POST'])
def calc():
    n1=int(request.form["num1"])
    n2=int(request.form ["num2"])
    op =request.form["operator"]
    return str(n1+n2) if op == "+" else str(n1-n2) if op == "-" else str(n1*n2) if op == "*" else str(n1/n2) if op =="/" else "Invalid"

if __name__ == "__main__":
    app.run(debug=True)