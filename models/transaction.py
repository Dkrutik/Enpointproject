from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from config import Config
from datetime import datetime

bcrypt = Bcrypt()

client = MongoClient(Config.MONGO_URI)
db = client.get_database()

class Transaction:
    @staticmethod
    def create_transaction(username, amount, type):
        db.transactions.insert_one({"username": username, "amount": amount, "type": type, "timestamp": datetime.now()})
    
    @staticmethod
    def get_transactions(username):
        # print(list(db.transactions.find({"username": username})))
        return list(db.transactions.find({"username": username}))
    
    @staticmethod
    def get_balance(username):
        transactions = Transaction.get_transactions(username)
        balance = sum(t['amount'] if t['type'] == 'deposit' else -t['amount'] for t in transactions)
        return balance
