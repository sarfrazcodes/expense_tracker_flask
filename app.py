from flask import Flask,render_template,redirect,request

app = Flask(__name__)
pocket_money = 0
expenses = []

@app.route("/",methods=["GET","POST"])
def landing():
    global pocket_money
    if request.method=="POST":
        pocket_money = int(request.form["pocket_money"])
        return redirect("/add-expense")
    
    return render_template("dashboard.html")

@app.route("/add-expense",methods=["GET","POST"])
def add_expense():
    global expenses
    if request.method=="POST":
        expense = {
            "category" : request.form["category"],
            "details" : request.form["details"],
            "amount" : int(request.form["amount"])
        }
        expenses.append(expense)
    return render_template("add_expense.html",expenses=expenses)

@app.route("/result")
def result():
    total_spent = sum(e["amount"] for e in expenses)
    remaining = pocket_money - total_spent

    return render_template("result.html",pocket_money=pocket_money,total_spent=total_spent,remaining=remaining)

if __name__ == "__main__":
    app.run(debug=True)