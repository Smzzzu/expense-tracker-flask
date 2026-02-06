from flask import Flask, render_template, request, redirect
from expense import Expense
from manager import ExpenseManager

app = Flask(__name__)
manager = ExpenseManager("expenses.csv")

@app.route("/")
def index():
    expenses = []
    with open("expenses.csv", "r") as file:
        for line in file.readlines()[1:]:
            expenses.append(line.strip().split(","))
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]

    expense = Expense(title, amount, category)
    manager.add_expense(expense)

    return redirect("/")

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

