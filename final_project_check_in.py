# INST326 Final project check-in (Group 6)

# Currently, everyone has written their own functions and classes that will 
# address certain challenges for the final project. Our next step is to analyze
# each member's code and find out how to make them function better with each 
# other and become one cohesive program.

import argparse

#Kirk Laryea
class FinanceManager:
    def __init__(self,filepath):
        self.filepath=filepath
        self.data=[]
    def load_data(self):
        try:
            with open(self.filepath,'r',encoding='utf-8') as f:
                self.data=[]
                for line in f.readlines():
                    content=line.strip().split(',')
                    self.data.append(content)
        except FileNotFoundError:
            print("This file does not exist, do you mean 'finance.txt?'")
                
                
#Kevin Pham
# Calculates total expenses by summing up expenses.
# Computes savings by subtracting total expenses from income.
# Constructs dictionary budget containing income, total expenses, and savings.
# Returns budget dictionary.
def budget_per_month(income, expenses):
    total_expenses = sum(expenses)
    savings = income - total_expenses
    
    budget = {
        "Income": income,
        "Total Expenses": total_expenses,
        "Savings": savings
    }
    
    return budget

# Prompts user to enter monthly income and number of expenses.
income = float(input("Please enter your monthly income ($): "))
num_expenses = int(input("Please enter the number of expenses that you have: "))

# Using a loop, it asks the user to enter the amount for each expense and stores 
# them in a list named expenses.
expenses = []
for exp in range(num_expenses):
    expense = float(input(f"Please enter the amount for expense #{exp+1}: "))
    expenses.append(expense)

# Calls budget_per_month function with provided income and expenses.
budget = budget_per_month(income, expenses)

# Iterates over the items in the budget dictionary and prints each category 
# (income, total expenses, savings) along with its corresponding amount.
print("\nSummary:")
for category, amount in budget.items():
    print(f"{category}:${amount:.2f}")
    
    
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

print(savings_goals_instance.money_goals())