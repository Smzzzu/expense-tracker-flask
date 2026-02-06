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

@app.route("/delete/<int:index>", methods=["POST", "GET"])

def add():
    title = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]

    expense = Expense(title, amount, category)
    manager.add_expense(expense)

    return redirect("/")
    @app.route("/delete/<int:index>", methods=["POST"])
    def delete(index):
        with open("expenses.csv", "r") as file:
            lines = file.readlines()

    header = lines[0]
    data = lines[1:]

    if 0 <= index < len(data):
        data.pop(index)

    with open("expenses.csv", "w") as file:
        file.write(header)
        file.writelines(data)

    return redirect("/")
    
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)



