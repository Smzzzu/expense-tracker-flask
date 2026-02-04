import csv

class ExpenseManager:
    def __init__(self, filename):
        self.filename = filename

    def add_expense(self, expense):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(expense.to_list())

    def view_expenses(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)