# INST326 Final project check-in (Group 6)

# Currently, everyone has written their own functions and classes that will 
# address certain challenges for the final project. Our next step is to analyze
# each member's code and find out how to make them function better with each 
# other and become one cohesive program.
#testing
import argparse

#Kirk Laryea      
class FinanceManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.statement = {}

    def set_statement(self, budget):
        self.statement = budget  
    def date(self):
        month = self.statement.get("Month", "N/A")
        day = self.statement.get("Day", "N/A")
        year = self.statement.get("Year", "N/A")
        return f"{month}/{day}/{year}"
    
    def save_data(self):
        try:
            with open(self.filepath, "a", encoding="utf-8") as file:
                seperator='- - - - - - - - - - - - - - - -'
                file.write(f'{seperator}\n')
                formatted_date=self.date()
                file.write(f"Budget Summary for {formatted_date}\n")
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
def budget_per_month(month,day,year,income, expenses):
    total_expenses = sum(expenses)
    savings = income - total_expenses
    
    budget = {
        "Month":month,
        "Day":day,
        "Year":year,
        "Income": income,
        "Total Expenses": total_expenses,
        "Savings": savings
    }
    
    return budget


months=["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]
month = input("Please enter the current month: ")
if month not in months:
    raise ValueError (f"Invalid month")
day = int(input("Please enter the current day of the month: "))
year=int(input("Please enter the current year: "))
income = float(input("Please enter your monthly income ($): "))
num_expenses = int(input("Please enter the number of expenses that you have: "))

expenses = []
for i in range(num_expenses):
    expense = float(input(f"Please enter the amount for expense #{i + 1}: "))
    expenses.append(expense)


budget = budget_per_month(month,day,year, income, expenses)
file_path = "finance.txt"  
budget_manager = FinanceManager(file_path)
budget_manager.set_statement(budget) 
budget_manager.save_data() 
    
    
#Miles Rousseau
from datetime import datetime

class findtransactions:
    # Kinda of works with hard-codes values (FOR NOW).
    # Goal is to do something like (python 'script-here' date 05-0x3-2024)


    def get_transactions(self, filter_type=None, filter_value=None):
        
        for entry in self.data:
         if entry['date']:
            entry['date'] = datetime.strptime(entry['date'])
            
        filtered_data = []
        if filter_type and filter_value:
            for entry in self.data:
                if filter_type == 'date' and entry['date'] == datetime.strptime(entry['date']):
                    filtered_data.append(entry)
                elif filter_type == 'amount' and float(entry['amount']) == float (filter_value):
                    filtered_data.append(entry)
                elif filter_type == 'type' and entry['type'] == filter_value:
                    filtered_data.append(entry)
        else:
            filtered_data = self.data
            
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