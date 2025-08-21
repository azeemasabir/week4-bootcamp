from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False, default=date.today)

    def __repr__(self):
        return f"<Expense {self.category} {self.amount} on {self.date}>"
