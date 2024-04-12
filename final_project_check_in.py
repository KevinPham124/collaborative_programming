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