# INST326 Final project check-in
import argparse

#Kirk Laryea
class FinanceManager:
    def __init(self,filepath):
        self.filepath=filepath
        self.data=[]
    def load_data(self):
        try:
            with open(self.filepath,'r',encoding='utf-8') as f:
                self.data=[]
                for line in f.readlines():
                    content=line.strip().splt(',')
                    self.data.append(content)
        except FileNotFoundError:
            print("This file does not exist, do you mean 'finance.txt?'")
                
#Kevin Pham
def add_budget():
    
    
#Miles Rousseau
def get_transactions():
    
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