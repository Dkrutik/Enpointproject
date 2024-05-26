from flask import request, jsonify, session
from models.transaction import Transaction

class TransactionController:
    @staticmethod
    def deposit():
        if 'username' not in session:
            return jsonify({"message": "Not logged in"}), 401
        data = request.get_json()
        Transaction.create_transaction(session['username'], data['amount'], 'deposit')
        return jsonify({"message": "Deposit successful"}), 200
    
    @staticmethod
    def withdraw():
        if 'username' not in session:
            return jsonify({"message": "Not logged in"}), 401
        data = request.get_json()
        balance = Transaction.get_balance(session['username'])
        if balance < data['amount']:
            return jsonify({"message": "Insufficient funds"}), 400
        Transaction.create_transaction(session['username'], data['amount'], 'withdraw')
        return jsonify({"message": "Withdrawal successful"}), 200
    
    @staticmethod
    def get_balance():
        if 'username' not in session:
            return jsonify({"message": "Not logged in"}), 401
        balance = Transaction.get_balance(session['username'])
        return jsonify({"balance": balance}), 200
    
    @staticmethod
    def get_transaction_history():
        if 'username' not in session:
            return jsonify({"message": "Not logged in"}), 401
        transactions = Transaction.get_transactions(session['username'])
        return jsonify({"transactions": transactions}), 200
