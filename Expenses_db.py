import pymongo 

class Expenses_db():
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client["expenses_database"]
        self.expenses_collection = self.database["expenses"]
        self.saldo_collection = self.database["saldos"]
        self.payments_collection = self.database["payments"]

    # Expenses
    def add_expense(self, person: str, expenses: float = 0.0):
        result = self.expenses_collection.find_one({'name': person}, {'expense': 1})
        if result:
            expense = result['expense']
            x = self.expenses_collection.update_one({'expense': expense}, {"$set": { "expense": expense + float(expenses)}})
            self.expenses_collection.find_one({'_id': x.upserted_id})
            resp = self.expenses_collection.find_one({'name': person})
        else:
            doc = {'name': person, 'expense': float(expenses)}
            x = self.expenses_collection.insert_one(document=doc)
            resp = self.expenses_collection.find_one({'_id': x.inserted_id})
        if resp:
            resp['_id'] = str(resp['_id'])
        return resp
        
    def get_expenses(self):
        return list(self.expenses_collection.find({}, {'expense': 1}))
    
    def get_expense(self, person: str):
        expense = self.expenses_collection.find_one({'name': person}, {'expense': 1})
        return expense if expense else 0.0
    
    def get_people(self):
        return list(self.expenses_collection.find({}, {'name': 1}))
    
    def get_expenses_collection(self):
        return self.expenses_collection.find({})
    
    def reset_expenses(self):
        self.expenses_collection.update_one({}, {"$set": { "expense": 0.0}})

    def reset_expense(self, person: str):
        result = self.expenses_collection.find_one({'name': person}, {'expense': 1})
        if result:
            self.expenses_collection.update_one({'expense': result}, {"$set": { "expense": 0.0}})

    # def save_expenses(self, file_name: str = 'expenses.json'):
    #     with open(file_name, "w") as outfile:
    #         json.dump(self.expenses_collection, outfile)

    # def load_expenses(self, file_name: str = 'expenses.json'):
    #     with open(file_name, "r") as infile:
    #         self.expenses_collection = json.load(infile)

    def get_total_expenses(self):
        return sum(self.expenses_collection.find({}, {'expense': 1}))
    
    # Saldos
    def split_expenses(self):
        total_expenses = self.get_total_expenses()
        num_people = len(self.get_people())
        exp_per_person = total_expenses / num_people
        for person in self.get_people():
            self.saldo_collection.insert_one({'name': person, 'saldo': exp_per_person - self.get_expense(person)})  # < 0: creditor, > 0: debtor
            self.payments_collection.insert_one({'name': person, 'payment_partner': {}})

    def get_saldo_collection(self):
        return self.saldo_collection.find({})
    
    def get_saldo(self, person: str):
        return self.saldo_collection.find_one({'name': person}, {'saldo': 1})
    
    def get_creditors(self):
        return self.saldo_collection.find({'saldo': { "$lt": 0.0 }}, {'name': 1})
    
    def get_debtors(self):
        return self.saldo_collection.find({'saldo': { "$gt": 0.0 }}, {'name': 1})
    
    # Who pays whom
    def get_payments_collection(self):
        return self.payments_collection.find({})   # {debtor: {creditor: amount}}
    
    # def get_payment_strategy(self):
    #     for debtor in self.get_debtors():
    #         for creditor in self.get_creditors():
    #             debt_to_pay = abs(self.get_saldo(debtor)['saldo'] - sum(self.payments_collection[debtor].values()))
    #             money_to_receive = abs(self.get_saldo(creditor)['saldo']) - sum(self.payments_collection[creditor].values())
    #             if (debt_to_pay == 0) or (money_to_receive == 0):
    #                 continue
    #             print('deptor: ', debtor, ', debt to pay: ', debt_to_pay, ', creditor: ', creditor, ', money left to receive: ', money_to_receive)
    #             money_exchanged = min(debt_to_pay, money_to_receive)
    #             self.payments_collection[debtor][creditor] = money_exchanged
    #             self.payments_collection[creditor][debtor] = money_exchanged

    # def get_payment_partner(self, person: str):
    #     return self.payments_collection.find_one({'name': person}, {'payment_partner': 1})['payment_partner']


if __name__ == '__main__':
    expense_db = Expenses_db()
    print(expense_db.client.list_database_names())
    expense_db.add_expense('Jorge', 10.0)
    expense_db.add_expense('Jorge', 20.0)
    expense_db.add_expense('Jan', 30.0)
    print(expense_db.get_expenses())
