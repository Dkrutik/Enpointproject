from flask import request, jsonify, session
from models.transaction import Transaction

class TransactionController:
    @staticmethod
    def deposit():
        print("dddddd--", session)
        if 'username' not in session:
            return jsonify({"message": "Not logged in"}), 401
        data = request.get_json()
        print("kkkk",data)
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
        sanitized_data = [
        {key: value for key, value in entry.items() if key != '_id'}
        for entry in transactions]
        return jsonify({"data": sanitized_data}), 200
        # return jsonify({"transactions": transactions}), 200


