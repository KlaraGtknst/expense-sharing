from flask import Flask, request
from flask_restx import Api, Resource
#from flask_cors import CORS
from ExpensesDictionary import *



'''
Run Backend using Flask: 
flask --app expense_server run --debug --port 5000
'''


app = Flask(__name__)
api = Api(app, version='1.0', title='Expense sharing', description='API of the project.')
#cors = CORS(app)

expense_dict = ExpensesDictionary()

person_description = {'person': {'description':'Name of person', 'type':'string'}}
expense_description = {'expense': {'description':'Expense of person', 'type':'float'}}

@api.doc(params=person_description | expense_description)
@api.route('/settings', endpoint='settings')
class Settings(Resource):
    
    def get(self):
        # http://127.0.0.1:5000/settings
        args = request.args
        person = args.get('person', default=None, type=str)

        if person:
            return expense_dict.get_expense(person)
        return expense_dict.get_expenses_dict()
    
    def put(self):
        args = request.args
        person = args.get('person', default=None, type=str)
        expense = args.get('expense', default=0.0, type=float)

        if person:
            expense_dict.add_expense(person, expense)
            return expense_dict.get_expense(person)


@api.doc(params=person_description)
@api.route('/split/saldos', endpoint='saldos')
class Saldos(Resource):
    def get(self):
        # http://127.0.0.1:5000/split/saldos
        args = request.args
        person = args.get('person', default=None, type=str)

        if person:
            return expense_dict.get_saldo(person)
        
        return expense_dict.get_saldo_dict()
    
        
@api.doc(params=person_description)
@api.route('/split/strategy', endpoint='strategy')
class Strategy(Resource):
    def get(self):
        # http://127.0.0.1:5000/split/strategy
        args = request.args
        person = args.get('person', default=None, type=str)

        if person:
            return expense_dict.get_payment_partner(person)
        
        return expense_dict.get_payments_dict()