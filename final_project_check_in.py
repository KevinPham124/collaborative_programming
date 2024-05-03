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
class Budget:
    def __init__(self):
        self.expenses = {}
        
    def set_budget(self, expense_category, amount):
        self.expenses[expense_category] = amount
        
    def get_budget(self, category):
        return self.expenses.get(category, 0)
 
    def delete_budget(self, category):
        if category in self.expenses:
            del self.expenses[category]
    
    
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