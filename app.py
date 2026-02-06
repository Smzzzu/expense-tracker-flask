from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

CSV_FILE = "expenses.csv"


# ---------------- HOME ----------------
@app.route("/")
def index():
    expenses = []

    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as file:
            lines = file.readlines()[1:]  # skip header
            for line in lines:
                expenses.append(line.strip().split(","))

    return render_template("index.html", expenses=expenses)


# ---------------- ADD EXPENSE ----------------
@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a") as file:
        if not file_exists:
            file.write("Title,Amount,Category\n")
        file.write(f"{title},{amount},{category}\n")

    return redirect("/")


# ---------------- DELETE EXPENSE ----------------
@app.route("/delete/<int:index>")
def delete(index):
    if not os.path.exists(CSV_FILE):
        return redirect("/")

    with open(CSV_FILE, "r") as file:
        lines = file.readlines()

    header = lines[0]
    data = lines[1:]

    if 0 <= index < len(data):
        data.pop(index)

    with open(CSV_FILE, "w") as file:
        file.write(header)
        file.writelines(data)

    return redirect("/")


# ---------------- RUN ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
