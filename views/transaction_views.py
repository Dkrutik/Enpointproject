from flask import Blueprint
from controllers.transaction_controller import TransactionController

transaction_bp = Blueprint('transaction_bp', __name__)

transaction_bp.route('/deposit', methods=['POST'])(TransactionController.deposit)
transaction_bp.route('/withdraw', methods=['POST'])(TransactionController.withdraw)
transaction_bp.route('/balance', methods=['GET'])(TransactionController.get_balance)
transaction_bp.route('/history', methods=['GET'])(TransactionController.get_transaction_history)
