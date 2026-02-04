# Expense class

class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

    def to_list(self):
        return [self.title, self.amount, self.category]