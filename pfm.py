# INST326 Final Project (Group 6) - Personal Finance Manager

class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount
        
    def __repr__(self):
        return f"Expense: '{self.name}' - [{self.category}, ${self.amount:.2f}]"

def main():
    print(f"-- Welcome to the Personal Finance Manager! --")
    file_path = input("Enter the file path where you want to save your expenses (ex: 'finance.txt'): ")
    budget = float(input("Enter your budget for this month ($): "))
    
    while True:
        expense = get_expense()
        
        save_expense(expense, file_path)
        
        summarize_expenses(file_path, budget)
        
        choice = input("Do you want to add more expenses, delete an expense, or exit the program? (add/delete/exit): ").lower()
        
        if choice == 'exit':
            break  
        
        if choice == 'delete':
            delete_expense(file_path)

def get_expense():
    print(f"Getting User Expense...")
    expense_name = input("Please enter the name of the expense you want to add: ")
    expense_amount = float(input("Please enter the amount of that expense ($): "))
    expense_categories = [
        "Home", 
        "Car",
        "Food",
        "Work",
        "Subscription",
        "Misc.",
    ]

    while True:
        print("Please select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}, {category_name}")
            
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Please enter a category number {value_range}: "))
                
        if selected_index in range(1, len(expense_categories) + 1):
            selected_category = expense_categories[selected_index - 1]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Please enter a valid category!")

def save_expense(expense: Expense, file_path):
    print(f"Saving User Expense: {expense} to {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def summarize_expenses(file_path, budget):
    print(f"Summarizing User Expense...")
    expenses = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(", ")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            print(line_expense)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses By Category: ")
    for key, amount in amount_by_category.items():
        print(f"    {key}: ${amount:.2f}")
        
    total_spent = sum(ex.amount for ex in expenses)
    print(f"You have spent {total_spent:.2f} this month!")
    
    remaining_budget = budget - total_spent
    print(f"Remaining Budget: {remaining_budget:.2f}")

def delete_expense(file_path):
    expense_to_delete = input("Please enter the name of the expense you want to delete: ")
    with open(file_path, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        new_lines = []
        deleted = False
        for line in lines:
            if expense_to_delete not in line:
                new_lines.append(line)
            else:
                deleted = True
        f.writelines(new_lines)

    if deleted:
        print(f"Expense '{expense_to_delete}' has been deleted.")
    else:
        print(f"Expense '{expense_to_delete}' not found.")

if __name__ == "__main__":
    main()

