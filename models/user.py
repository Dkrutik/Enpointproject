from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from config import Config

bcrypt = Bcrypt()

client = MongoClient(Config.MONGO_URI)
db = client.get_database()

class User:
    @staticmethod
    def create_user(username, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        db.users.insert_one({"username": username, "password": hashed_password})
    
    @staticmethod
    def find_user(username):
        return db.users.find_one({"username": username})
    
    @staticmethod
    def verify_password(stored_password, provided_password):
        return bcrypt.check_password_hash(stored_password, provided_password)
