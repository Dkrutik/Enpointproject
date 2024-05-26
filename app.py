from flask import Flask, session
from config import Config
from views.user_views import user_bp
from views.transaction_views import transaction_bp

app = Flask(__name__)


# @app.route("/data/")
# def add():
#     return jsonify({"name":"rutik","age":24})
app.config.from_object(Config)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(transaction_bp, url_prefix='/transaction')


if __name__ == "__main__":
    app.run(debug=True)