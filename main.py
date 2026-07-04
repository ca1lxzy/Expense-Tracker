from database.db import Database
from models.expense import Expense

def menu():
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")

db = Database()

while True:
    menu()

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        date = input("Date (YYYY-MM-DD): ")

        expense = Expense(title, category, amount, date)
        db.add_expense(expense)

    elif choice == "2":
        expenses = db.get_expenses()

        print("\n------ Expenses ------")
        for row in expenses:
            print(row)

    elif choice == "3":
        expense_id = int(input("Expense ID: "))
        title = input("New Title: ")
        category = input("New Category: ")
        amount = float(input("New Amount: "))
        date = input("New Date: ")

        db.update_expense(expense_id, title, category, amount, date)

    elif choice == "4":
        expense_id = int(input("Expense ID: "))
        db.delete_expense(expense_id)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")