# INST326 Final project check-in (Group 6)

# Currently, everyone has written their own functions and classes that will 
# address certain challenges for the final project. Our next step is to analyze
# each member's code and find out how to make them function better with each 
# other and become one cohesive program.

import argparse
import sys
from datetime import datetime

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


class findtransactions:
    """
    
    Place Holder
    
    """


    def __init__(self, filepath):
        self.filepath = filepath
        

    def get_transactions(self, filter_type=None, filter_value=None):
        
        data = FinanceManager(self.path).load_data()
        filtered_data = []
        for entry in data:
            if entry['date']:
                entry['date'] = datetime.strptime(entry['date'], '%m%Y').date()
            entry['Income'] = float(entry['Income'].replace('$', '').replace(',', ''))
            entry['Total Expenses'] = float(entry['Total Expenses'].replace('$', '').replace(',', ''))
            entry['Savings'] = float(entry['Savings'].replace('$', '').replace(',', ''))


                
        if filter_type and filter_value:
            for entry in data:
                if filter_type == 'date' and entry['date'] == datetime.strptime(filter_value, '%m%Y').date():
                    filtered_data.append(entry)
                elif filter_type == 'income' and float(entry['Income']) == float (filter_value):
                    filtered_data.append(entry)
                elif filter_type == 'savings' and entry['Savings'] == filter_value:
                    filtered_data.append(entry)
                elif filter_type == 'total_expenses' and entry ['Total Expenses'] == float(filter_value):
                    filtered_data.append(entry)
        else:
            filtered_data = self.statement   
        return filtered_data
    
    
#Bryan Moody
class SortedSavingsGoals:
    def __init__(self, goals, income, savings = 0, \
        sort_by = 'still needed'):
        self.goals = goals
        self.income = income
        self.savings = savings
        self.sort_by = sort_by

    def monthly_savings_calc(self, goal):
        remaining_to_goal = goal - self.savings
        monthly_savings_needed = remaining_to_goal / 12
        return {
            'savings needed': monthly_savings_needed,
            'how much of income is needed': 
                ((monthly_savings_needed / self.income) * 100)
        }

    def money_goals(self):
        end_results = [self.monthly_savings_calc(goal) \
            for goal in self.goals]
        key = 'savings needed' if self.sort_by == 'still needed' \
            else 'how much of income is needed'
        end_results.sort(key = lambda var: var[key], reverse = True)
        return end_results
        
goals = [5000, 10000, 15000]
income = 3000
savings = 500

sort_by = 'percentage'
savings_goals_instance = SortedSavingsGoals(goals, income, savings, sort_by)

#print(savings_goals_instance.money_goals())

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