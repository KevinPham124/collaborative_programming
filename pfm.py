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
    
    
#Miles Rousseau


class FindTransactions:
    """
    A class for searching specific budget summaries.
    
    Attributes:
        filepath(str): The file path of the budget summary file. (Finance.txt)
    
    """

    def __init__(self, filepath):
        """
        Initializes the FindTransactions object with given file path.
        
        Parameters:
            filepath(str): The file path of the budget summary file. (Finance.txt)
        """
     
        self.filepath = filepath

    def search_budget_summary(self, target_date):
        """
        Searches for a budget summary for the specified date and print it if found!
        
        Parameters:
            target_date(str): The target date in the format "Month/Year"

        
        """
        with open(self.filepath, 'r') as file:
            found = False
            for line in file:
                if f"Budget Summary for {target_date}" in line:
                    found = True
                    print(line.strip())  
                    for _ in range(3):  
                        print(next(file).strip())
                    print("-" * 30)  
            if not found:
                print("No budget summary found for the specified date.")
        
    
#Miles Rousseau

class DataVisualizer:
    """
   This class is for visualizing the budgets using a bar plot.
   
   Attributes:
        filepath(str): The file path of the budget summary file. (Finance.txt)
    """
    def __init__(self, filepath):
        """
        Initializes the DataVisualizer object with the given file path.
        
        Parameters:
            filepath(str): The file path of the budget summary file. (Finance.txt)
        """
        self.filepath = filepath

    def visualize_between_years(self, start_year, end_year):
        """
       Visualizes the financial data between specific years.
       
       Parameters:
            start_year(int): The start of the year for filtering the data.
            end_year(int): The end year for filtering the data.
        """
        try:
            financial_data = self.read_financial_data()
            filtered_data = self.filter_data_by_years(financial_data, start_year, end_year)
            self.plot_data(filtered_data, start_year, end_year)
        except Exception as e:
            print("An error occurred during visualization:", e)

    def read_financial_data(self):
        """
        Reads the financial data from the file.
        
        Returns:
            Returns a list of dictonaries that represents the financial data.
        """

        with open(self.filepath, 'r') as file:
            financial_data = []
            for line in file:
                if "Budget Summary for" in line:
                    entry = {}
                    entry["Year"] = int(line.split("/")[-1].strip())
                    for _ in range(3):
                        line = next(file).strip()
                        key, value = line.split(": ")
                        entry[key] = float(value.strip("$"))
                    financial_data.append(entry)
        return financial_data

    def filter_data_by_years(self, financial_data, start_year, end_year):
        """
        Filters financial data to include only data between specified years in finance.txt
        
        Parameters:
            financial_data(list): A list of dictonaries that represents financial data.
            start_year(int): The start of the year for filtering the data.
            end_year(int): The end year for filtering the data.
            
        Returns:
            Also returns a list of dictonaries that represents the financial data.
        
        """
        return [entry for entry in financial_data if start_year <= entry["Year"] <= end_year]

    def plot_data(self, data, start_year, end_year):
        """
        Creates a bar plot of the persons budget savings from finance.txt
        
        Parameters:
            data (list): A list of dictionaries representing the financial data.
            start_year(int): The start of the year for filtering the data.
            end_year(int): The end year for filtering the data.
            
        """
        years = [entry["Year"] for entry in data]
        savings = [entry["Savings"] for entry in data]

        plt.bar(years, savings, color='skyblue')
        plt.xlabel('Years')
        plt.ylabel('Your Savings ($)')
        plt.title('Savings Comparison between {} and {}'.format(start_year, end_year))
        plt.yticks(range(0, int(max(savings)) + 1000, 1000))
        plt.show()



#Bryan Moody
class SavingsCalculator:
    """
    Calculator for determining how much money to be saved each month
    
    Attributes:
        finance_goal (int): The amount of money you want to reach
        income (int): Individual monthly income
        savings (int): How much savings do the individuals have?
    
    """
    def __init__(self, finance_goal, income, savings = 0):
        """
        Initializes a specified financial goal, income, and savings
        
        Parameters:
            goals(list): Financial Target
            income (int): Monthly wage
            savings(int): How much is in the individual's savings account
            
        """
        self.finance_goal = finance_goal
        self.income = income
        self.savings = savings
        
    def monthly_savings_calc(self):
        """
        Monthly amount needed to be saved to reach financial goal in 12 months
        
        Returns:
            A dictionary with monthly savings, percentage of monthly income, and
            a feasible statement that returns true if savings required is less
            than or equal to 50 percent of monthly income.
        """
        remaining_to_goal = self.finance_goal - self.savings
        time_frame_months = 12
        monthly_savings_needed = remaining_to_goal / time_frame_months
        percentage_of_income = (monthly_savings_needed / self.income) * 100
        return {
            "monthly_savings_needed": monthly_savings_needed,
            "percentage_of_income": percentage_of_income,
            "feasible": percentage_of_income <= 50
        }

class SavingsGoals(SavingsCalculator):
    """
    Child class for sorting
    
    Attributes:
        goals (list): finacial goals
        sort_by (str): 'needed' or 'percentage' criterion to sort by
    """
    def __init__(self, goals, income, savings = 0, sort_by = "needed"):
        """
        Initializes class with goals, income, and savings lists
        
        Parameters:
            goals (int): Financial goals
            income (int): Monthly wages
            savings (int): How much is in the individual's savings account
            sort_by (str): 'needed' or 'percentage' criterion to sort by
        """
        super().__init__(0, income, savings)
        self.goals = goals
        self.sort_by = sort_by

    def money_goals(self):
        """
        Calculates monthly savings needed for each goal
        
        Returns:
            List of dictionaries
        """
        end_results = []
        for goal in self.goals:
            self.finance_goal = goal
            result = self.monthly_savings_calc()
            result['goal'] = goal
            end_results.append(result)

        if self.sort_by == "needed":
            end_results.sort(key = lambda var: var['monthly_savings_needed'], reverse=True)
        elif self.sort_by == "percentage":
            end_results.sort(key = lambda var: var['percentage_of_income'], reverse=True)

        return end_results

if __name__ == "__main__":
    goals_input = input("What is your financial goal? (ex: 250000): ")
    monthly_income_input = int(input("What is your monthly income? (ex: 1000): "))
    personal_savings_input = int(input("How much do you currently have in savings? (ex: 500): ") or 0)
    sorted = input("Please enter a sorting criterion ('needed' or 'percentage') ") or "needed"

    goals = list(map(int, goals_input.split('.')))

    calculator = SavingsGoals(goals, monthly_income_input, personal_savings_input, sorted)
    sorted_goals = calculator.money_goals()

    for goal in sorted_goals:
        print(f"Goal: ${goal['goal']} - Monthly Savings Needed: ${goal['monthly_savings_needed']:.2f}, "
              f"Percentage of Monthly Income: {goal['percentage_of_income']:.2f}%, "
              f"Feasibility: {'Yes' if goal['feasible'] else 'No'}")
        
        

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
