# INST326 Final Project (Group 6) - Personal Finance Manager

import argparse

#Kirk Laryea      
class Expense:
    '''
    A class to represent a single financial expense.

    Attributes:
        name (str): The name of the expense (e.g.mcdonalds).
        category (str): The category of the expense (e.g.'Food').
        amount (float): Theamount of the expense.

    Methods:
        __repr__(): Returns a string representation of the expense including the name, category, and amount.
    '''
    def __init__(self, name, category, amount):
         '''
        Initializes the Expense class with a name, category, and amount.

        Args:
            name (str): The name of the expense.
            category (str): The category to which the expense belongs.
            amount (float): The cost of the expense.
        '''
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        '''
        Provides a string representation of the expense, including its name, category, and amount.

        Returns:
            str: A formatted string showing the name, category, and amount of the expense.
        '''
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
    '''
    Prompts the user to input the details of an expense and creates an Expense object.
    
    Returns:
        Expense: An instance of the Expense class with the specified name, category, and amount.
    
    Raises:
        ValueError: If the selected category index is not within the valid range.
    '''
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


def main(output_file):
    '''
    This function collects input from the user to be stored in the output file.
    It also compares and shows  the user data summaries.
    Args:
       output_file(str): The file  were summaries are stored 
    Raises:
        ValueError:If user inputs invalid month
        Exception: If an inexpected error occurs
    Side efffects;
        -Reads data form output_file and prints summary.
        -Creates instances of the FInanceMannager class.
    '''
    months=['01', '02', '03', '04','05','06','07','08','09','10','11','12']
    try:
        month = input("Please enter the current month: ")
        if month not in months:
            raise ValueError (f"Invalid month, try again")
        year=int(input("Please enter the current year: "))
        income = float(input("Please enter your monthly income ($): "))
        num_expenses = int(input("Please enter the number of expenses that you have: "))

        expenses = []
        for i in range(num_expenses):
            expense = float(input(f"Please enter the amount for expense #{i + 1}: "))
            expenses.append(expense)

        budget = budget_per_month(month,year, income, expenses)
        budget_manager = FinanceManager(output_file)
        budget_manager.set_statement(budget) 
        budget_manager.save_data() 
        
        view_summaries = input("Would you like to view any budget summaries? (yes/no): ")
        if view_summaries.lower() == 'yes':
            finder = FindTransactions(output_file)
            target_date = input("Enter the date (MM/YYYY) to search for budget transactions: ")
            finder.search_budget_summary(target_date)
        else:

            print("No problem!")
            
            
        compare_years = input("Would you like to compare savings goals from different years? (yes/no): ")
        if compare_years.lower() == 'yes':
            start_year = int(input("Enter the start year for comparison: "))
            end_year = int(input("Enter the end year for comparison: "))
            print("Thank you for using our budget summary tracker! Here is budget comparison using a bar plot!")
            visualizer = DataVisualizer(output_file)
            visualizer.visualize_between_years(start_year, end_year)
            
        else:

            print("Thank you for using our budget summary tracker!")
        
    except ValueError as ve:
        print("Input error:", ve)

    except Exception as e:
        print("An unexpected error occurred:", e)
    
def parse_args(arglist):
    '''Parse command-line arguments.
    Only one argument is required:
        output_file(str): Path to file were summaries are stored.
    Args:
        arglist (list of str): list of command-line arguments.
    Returns:
        namespace: the parsed arguments as a namespace. The following attribute
        will be defined: output_file.

    '''
    parser = argparse.ArgumentParser("Finance manager")
    parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    main()
