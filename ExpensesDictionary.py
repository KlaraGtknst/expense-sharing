import json


class ExpensesDictionary():
    '''
    class to store expenses of people
    '''
    def __init__(self) -> None:
        self.expenses_dict = {}
        pass

    def add_expense(self, person: str, expenses: float = 0.0):
        if person in self.expenses_dict.keys():
            self.expenses_dict[person] += float(expenses)
        else:
            self.expenses_dict[person] = float(expenses)
        
    def get_expenses(self):
        return list(self.expenses_dict.values())
    
    def get_expense(self, person: str):
        return self.expenses_dict[person] if person in self.expenses_dict.keys() else 0.0
    
    def get_people(self):
        return list(self.expenses_dict.keys())
    
    def get_expenses_dict(self):
        return self.expenses_dict
    
    def reset_expenses(self):
        self.expenses_dict = dict.fromkeys(self.expenses_dict, 0.0)

    def reset_expense(self, person: str):
        if person in self.expenses_dict.keys():
            self.expenses_dict[person] = 0.0 

    def save_expenses(self, file_name: str = 'expenses.json'):
        with open(file_name, "w") as outfile:
            json.dump(self.expenses_dict, outfile)

    def load_expenses(self, file_name: str = 'expenses.json'):
        with open(file_name, "r") as infile:
            self.expenses_dict = json.load(infile)




if __name__ == '__main__':
    expense_dict = ExpensesDictionary()
    print('hi, ' + str(expense_dict.get_expenses_dict()))