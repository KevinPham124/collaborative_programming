# INST326 Final project check-in (Group 6)

# Currently, everyone has written their own functions and classes that will 
# address certain challenges for the final project. Our next step is to analyze
# each member's code and find out how to make them function better with each 
# other and become one cohesive program.


import argparse
import sys

#Kirk Laryea      
class FinanceManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.statement = {}

    def set_statement(self, budget):
        self.statement = budget  
    def date(self):
        month = self.statement.get("Month")
        year = self.statement.get("Year")
        return f"{month}/{year}"
    
    def save_data(self):
        try:
            with open(self.filepath, "a", encoding="utf-8") as file:
                seperator='- - - - - - - - - - - - - - - -'
                file.write(f'{seperator}\n')
                file.write(f"Budget Summary for {self.date()}\n")
                file.write(f"Income: ${self.statement['Income']:.2f}\n")
                file.write(f"Total Expenses: ${self.statement['Total Expenses']:.2f}\n")
                file.write(f"Savings: ${self.statement['Savings']:.2f}\n")
            print("Budget summary saved successfully.")
        except Exception as e:
            print("Error saving data:", e)        
                
#Kevin Pham
# Calculates total expenses by summing up expenses.
# Computes savings by subtracting total expenses from income.
# Constructs dictionary budget containing income, total expenses, and savings.
# Returns budget dictionary.
def budget_per_month(month,year,income, expenses):
    total_expenses = sum(expenses)
    savings = income - total_expenses
    
    budget = {
        "Month":month,
        "Year":year,
        "Income": income,
        "Total Expenses": total_expenses,
        "Savings": savings
    }
    
    return budget
    
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
    months=["January",'01', "February",'02', "March",'03', "April",'04',
            "May",'05',"June",'06',"July",'07', "August",'08', "September",'09',
            "October",'10',"November",'11',"December",'12']
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
            print("Thank you for using our budget summary tracker!")
        
    except ValueError as ve:
        print("Input error:", ve)

    except Exception as e:
        print("An unexpected error occurred:", e)
    
def parse_args(arglist):
    parser = argparse.ArgumentParser("Finance manager")
    parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args=parse_args(sys.argv[1:])
    main(args.output_file)