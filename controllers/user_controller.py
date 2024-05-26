import traceback
from flask import request, jsonify, session
from models.user import User

from werkzeug.security import generate_password_hash, check_password_hash



class UserController:
    # @staticmethod
    # def login():
    #     data = request.get_json()
    #     user = User.find_user(data['username'])
    #     if user and User.verify_password(user['password'], data['password']):
    #         session['username'] = data['username']
    #         return jsonify({"message": "Login successful"}), 200
    #     return jsonify({"message": "Invalid credentials"}), 401
    
    @staticmethod
    def login():
        try:
            data = request.get_json()
            user = User.find_user(data['username'])
            if user and User.verify_password(user['password'], data['password']):
                session['username'] = data['username']
                return jsonify({"message": "Login successful"}), 200
            return jsonify({"message": "Invalid credentials"}), 401
        except Exception as e:
            return jsonify({"message": str(e)}), 500
        
    @staticmethod
    def register():
        try:
            data = request.get_json()
            if User.find_user(data['username']):
                return jsonify({"message": "User already exists"}), 409
            User.create_user(data['username'], data['password'])
            return jsonify({"message": "User created successfully"}), 201
        except Exception as e:
            traceback.print_exc()
            return jsonify({"message": str(e)}), 500
    
    
    @staticmethod
    def logout():
        session.pop('username', None)
        return jsonify({"message": "Logged out"}), 200
