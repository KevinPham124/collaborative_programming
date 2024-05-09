import matplotlib.pyplot as plt
# Group 6 Project.
class Expense:
    """
    A class to represent a single financial expense.
    
    Attributes:
        name (str): The name of the expense (e.g.mcdonalds)
        category(str): The category of the expense (e.g'Food').
        amount(float): The amount of the expense.
        
    Methods:
        __repr__(): Returns a string representation of the expense including name,
        category, and amount.
    
    """
    def __init__(self, name, category, amount):
        """
        Initializes the Expense class with a name, category, and amount.
        
        Args:
            name(str): The name of the expense.
            category(str): The category to which the expense belongs.
            amount(float): The cost of the expense.
        
        """
        self.name = name
        self.category = category
        self.amount = amount
        
    def __repr__(self):
        return f"Expense: '{self.name}' - [{self.category}, ${self.amount:.2f}]"

def main():
    """
    Manages user's finances by tracking expenses and calculating budget.
    
    Usage:
        1. Prompts the user to enter a file path where they want to save their expenses.
        2. Enter a budget amount for the month.
        3. Add expenses, delete expenses, or exit the program based on user choice.
        4. If choosing to delete, it prompts for which expense to remove.
    
    Returns:
        None
    """
    print(f"-- Welcome to the Personal Finance Manager! --")
    file_path = input("Enter the file path to save your expenses (e.g.: 'finance.txt'): ")
    budget = float(input("Enter your budget for this month: "))
    
    while True:
        expense = get_expense()
        
        save_expense(expense, file_path)
        
        sort_expenses_by_category(file_path)
        amount_by_category = summarize_expenses(file_path, budget)
        
        graph_choice = input("Would you like to see a graph of your expenses for this month? (yes/no): ").lower()
        if graph_choice == "yes":
            generate_bar_graph(amount_by_category)
        elif graph_choice == "no":
            pass
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue
        
        choice = input("Would you like to add more expenses, delete an expense, or exit the program? (add/delete/exit): ").lower()
        
        if choice == 'exit':
            break  
        
        if choice == 'delete':
            delete_expense(file_path)

def get_expense():
    """
    Prompts the user to input the details of an expense and creates an Expense object.
    
    Returns:
        Expense: An instance of the Expense class with the specified name, category, and amount.
    
    Raises:
        ValueError: If the selected category index is not within the valid range.
    """
    print(f"Getting User Expense...")
    expense_name = input("Please enter the name of the expense you want to add: ")
    expense_amount = float(input("Please enter the amount of that expense: "))
    expense_categories = [
        "Food", 
        "Home",
        "Work",
        "Fun",
        "Subscription",
        "Car",
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
    """
    This method saves the expense record to a file

    Parameters:
        espense (Expense): an instance of the Ecpence class containing the saved details
        file_path(str): The path to a file where the espense record will be appended or created

    Side Effects :
        Edits file_path with espense data
    """
    print(f"Saving User Expense: {expense} to {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def summarize_expenses(file_path, budget):
    """
    Summarizes user expenses from a specified file and calculates the total spent,
    expenses by category, and remaining budget.

    Args:
        file_path (str): Path to the file containing expense records.
        budget (float): Total budget amount for the month.

    Returns:
        None: This function does not return any value but prints a summary of expenses.
    """
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
    if not expenses:
        print ("No record")
        return {}

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
    
    return amount_by_category

def generate_bar_graph(amount_by_category):
    """
    Miles Rousseau
    
    Visualizes the budgets using a bar plot
    
    Parameters:
        amount_by_category (dict): A dictonary that contains expenses
        grouped by the category. (Fun, Work, Misc, Home, Food)
    
    Returns:
        None
    
    """
    categories = list(amount_by_category.keys())
    amounts = list(amount_by_category.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Expense Categories')
    plt.ylabel('Amount Spent ($)')
    plt.title('Expenses by Category')
    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()


def sort_expenses_by_category(file_path):
    """
    Miles Rousseau
    
    Sorting the expenses within the file by the category.
    Rewrites the file.
    
    Parameters:
    filepath(str): The path to the file
    
    Returns:
        None
        
    """
    category_expenses = {}
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(", ")
            expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            if expense.category in category_expenses:
                category_expenses[expense.category].append(expense)
            else:
                category_expenses[expense.category] = [expense]

    for category in category_expenses:
        category_expenses[category].sort(key=lambda x: x.name.lower())

    with open(file_path, "w") as f:
        for category in sorted(category_expenses.keys()):
            for expense in category_expenses[category]:
                f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def delete_expense(file_path):
    """
    This function deletes an unwanted expense entry from the file based on the name that is provided

    Parameters:
        file_path (str): The path to the file that the expanse entry is supposed to be deleted from
    
    Side Efects:
        Modifies the file_path by removing the espense entry based on user input
    """
    expense_to_delete = input("Please enter the name of the expense you want to delete: ")
    with open(file_path, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        new_lines = []
        deleted = any(expense_to_delete in line for line in lines) 
        new_lines = [line for line in lines if expense_to_delete not in line] 
        f.truncate(0)  
        f.writelines(new_lines)

    print(f"Expense '{expense_to_delete}' {'has been deleted.' if deleted else 'not found.'}")

if __name__ == "__main__":
    main()
