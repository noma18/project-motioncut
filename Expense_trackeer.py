# This python code enables user to maintain their expenses on daily basis and provides an interface to get the insights from previously stored records


import os
import json
import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):        
        if os.path.exists('expenses.json'):
            with open('expenses.json', 'r') as f:
                expenses = json.load(f)
                for date in list(expenses.keys()):
                    year, month, day = date.split()
                    new_date = f"{year}-{month}-{day}"
                    expenses[new_date] = expenses.pop(date)
                return expenses
        else:
            return {}

    def save_expenses(self):       #to save the enteries by user in expenses.json file
        with open('expenses.json', 'w') as f:
            json.dump(self.expenses, f)

    def add_expense(self):            # to add expenses entries by the user
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        category = input("Enter category: ")

        date = f"{year}-{month:02d}-{day:02d}"

        if date not in self.expenses:
            self.expenses[date] = []

        self.expenses[date].append({
            'amount': amount,
            'description': description,
            'category': category
        })

        self.save_expenses()

    def view_monthly_expenses(self):        # to view monthly expenses
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))

        total_amount = 0
        for date in self.expenses:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            if date_obj.year == year and date_obj.month == month:
                for expense in self.expenses[date]:
                    total_amount += expense['amount']
                    print(f"Date: {date}, Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")

        print(f"Total amount for the month: {total_amount}")

    def run(self):
        while True:
            print("1. Add expense")
            print("2. View monthly expenses")
            print("3. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_monthly_expenses()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
