import json


class ExpensesDictionary():
    '''
    class to store expenses of people
    '''
    def __init__(self) -> None:
        self.expenses_dict = {}
        self.saldo_dict = {}
        self.payments_dict = {}
        pass

    # Expenses
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

    def get_total_expenses(self):
        return sum(self.expenses_dict.values())
    
    # Saldos
    def split_expenses(self):
        total_expenses = self.get_total_expenses()
        num_people = len(self.get_people())
        exp_per_person = total_expenses / num_people
        for person in self.get_people():
            self.saldo_dict[person] = exp_per_person - self.get_expense(person) # < 0: creditor, > 0: debtor
            self.payments_dict[person] = {}

    def get_saldo_dict(self):
        return self.saldo_dict
    
    def get_saldo(self, person: str):
        return self.saldo_dict[person] if person in self.saldo_dict.keys() else 0.0
    
    def get_creditors(self):
        return [person for person in self.get_people() if self.get_saldo(person) <= 0]
    
    def get_debtors(self):
        return [person for person in self.get_people() if self.get_saldo(person) > 0]
    
    # Who pays whom
    def get_payments_dict(self):
        return self.payments_dict   # {debtor: {creditor: amount}}
    
    def get_payment_strategy(self):
        for debtor in self.get_debtors():
            for creditor in self.get_creditors():
                debt_to_pay = abs(self.get_saldo(debtor) - sum(self.payments_dict[debtor].values()))
                money_to_receive = abs(self.get_saldo(creditor)) - sum(self.payments_dict[creditor].values())
                if (debt_to_pay == 0) or (money_to_receive == 0):
                    continue
                print('deptor: ', debtor, ', debt to pay: ', debt_to_pay, ', creditor: ', creditor, ', money left to receive: ', money_to_receive)
                money_exchanged = min(debt_to_pay, money_to_receive)
                self.payments_dict[debtor][creditor] = money_exchanged
                self.payments_dict[creditor][debtor] = money_exchanged

    def get_payment_partner(self, person: str):
        return self.payments_dict[person]
            
             








if __name__ == '__main__':
    expense_dict = ExpensesDictionary()
    print('hi, ' + str(expense_dict.get_expenses_dict()))