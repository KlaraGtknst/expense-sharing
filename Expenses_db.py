import pymongo 

class Expenses_db():
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client["expenses_database"]
        self.expenses_collection = self.database["expenses"]
        self.saldo_collection = self.database["saldos"]
        self.payments_collection = self.database["payments"]

    # Expenses
    def add_expense(self, person: str, expense: float = 0.0):
        result = self.expenses_collection.find_one({'name': person}, projection={'expense': True})
        if result:
            old_expense = result['expense']
            x = self.expenses_collection.update_one({'name': person}, {"$set": { "expense": old_expense + float(expense)}})
            self.expenses_collection.find_one({'_id': x.upserted_id})
            resp = self.expenses_collection.find_one({'name': person})
        else:
            doc = {'name': person, 'expense': float(expense)}
            x = self.expenses_collection.insert_one(document=doc)
            resp = self.expenses_collection.find_one({'_id': x.inserted_id})
        return self.refactor_return_id(resp)
    
    def refactor_return_id(self, resp):
        if resp:
            resp['_id'] = str(resp['_id'])
        return resp
        
    def get_expenses(self):
        return [doc['expense'] for doc in self.expenses_collection.find({}, {'expense': 1})]
    
    def get_expense_by_name(self, person: str):
        expense = self.expenses_collection.find_one({'name': person}, {'expense': 1})
        return expense['expense'] if expense else 0.0
    
    def get_people(self):
        return [{doc['name']: str(doc['_id'])} for doc in self.expenses_collection.find({}, {'name': 1})]
    
    def get_expenses_collection(self):
        resp = [{'_id': str(doc['_id']), 'name': doc['name'], 'expense': doc['expense']} for doc in self.expenses_collection.find({})]
        return resp
    
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
        return sum([doc['expense'] for doc in self.expenses_collection.find({}, {'expense': 1})])
    
    # Saldos
    def split_expenses(self):
        total_expenses = self.get_total_expenses()
        people = self.get_people()
        num_people = len(people)
        exp_per_person = total_expenses / max(num_people, 1)
        for person in people:
            name = list(person.keys())[0]
            expense = self.get_expense_by_name(name)
            self.saldo_collection.insert_one({'_id': person[name], 'name': name, 'saldo': exp_per_person - expense})  # < 0: creditor, > 0: debtor
            self.payments_collection.insert_one({'_id': person[name], 'name': name, 'payment_partner': {}})

    def delete_old_dbs(self):
        self.saldo_collection.delete_many({})
        self.payments_collection.delete_many({})

    def get_saldo_collection(self):
        try:
            self.split_expenses()
        except:
            self.delete_old_dbs()
            self.split_expenses()
        return [{'_id': str(doc['_id']), 'name': doc['name'], 'saldo': doc['saldo']} for doc in self.saldo_collection.find({})]
    
    def get_saldo(self, person: str):
        try:
            self.split_expenses()
        except:
            self.delete_old_dbs()
            self.split_expenses()
        resp = self.saldo_collection.find_one({'name': person}, {'saldo': 1})
        return resp if resp else {'saldo': 0.0}
    
    def get_creditors(self):
        return [doc['name'] for doc in self.saldo_collection.find({'saldo': { "$lt": 0.0 }}, {'name': 1})]
    
    def get_debtors(self):
        return [doc['name'] for doc in self.saldo_collection.find({'saldo': { "$gt": 0.0 }}, {'name': 1})]
    
    # Who pays whom
    def get_payments_collection(self):
        return [{'_id': str(doc['_id']), 'name': doc['name'], 'payment_partner': doc['payment_partner']} for doc in self.payments_collection.find({})]
    
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
    print('Running Expenses_db.py')
    expense_db = Expenses_db()
    print(expense_db.client.list_database_names())
    expense_db.add_expense('Jorge', 10.0)
    expense_db.add_expense('Jorge', 20.0)
    expense_db.add_expense('Jan', 30.0)
    print(expense_db.get_expenses())
