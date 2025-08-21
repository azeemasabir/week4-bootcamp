from flask import Flask
from models import db
from routes import init_routes
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change-me'  # needed for flash messages later if you add them

    # SQLite DB in project folder
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'expense.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    init_routes(app)          # register routes

    with app.app_context():
        db.create_all()       # create tables if not exist

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
