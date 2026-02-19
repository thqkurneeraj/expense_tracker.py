class ExpenseTracker:
    def __init__(self):
        self.expenses=[]

    def add_expense(self):
        try:
            amount=float(input("Enter Amount: "))
            category=input("Enter category: ")

            expense= {"amount" : amount , "category" : category}
            self.expenses.append(expense)  

            print("Expense was added successfully")

        except ValueError:
            print("Invalid ampunt entered")

    def show_expenses(self):
        if len(self.expenses) == 0 :
            print("No expenses found")
            return
   
        print("\n--- Expense List ---")
    
        i = 1
        for exp in self.expenses:
            print(i, ".", exp["category"], ":", "₹", exp["amount"])
            i += 1

    def total_expense(self):
        total = 0
        for exp in self.expenses:
            total += exp["amount"]

        print("\nTotal Expense = ₹" ,total)

    def save_to_file(self):
        file = open("expensetracker.py" , "w")
        for exp in self.expenses:
            file.write(exp["category"] + "-" + str(exp["amount"])+ "\n")
            file.close()
            print("Expenses saved to file")

tracker = ExpenseTracker()

while True:
    print("\n----------Expense Tracker Menu----------")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total Expense")
    print("4. Save to File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.show_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        tracker.save_to_file()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")            


           