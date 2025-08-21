from flask import render_template, request, redirect, url_for
from models import db, Expense
from datetime import date, datetime
from sqlalchemy import func

CATEGORIES = ["Food", "Transport", "Rent", "Utilities", "Health", "Shopping", "Entertainment", "Other"]

def _month_bounds(yyyy_mm: str | None):
    """Return (start_date, end_date_exclusive) for a YYYY-MM string or current month if None."""
    if not yyyy_mm:
        today = date.today()
        start = today.replace(day=1)
    else:
        start = datetime.strptime(yyyy_mm, "%Y-%m").date().replace(day=1)
    # next month
    if start.month == 12:
        next_month = start.replace(year=start.year + 1, month=1, day=1)
    else:
        next_month = start.replace(month=start.month + 1, day=1)
    return start, next_month

def init_routes(app):
    @app.route("/", methods=["GET"])
    def index():
        # Optional month filter from query (?month=YYYY-MM)
        month_str = request.args.get("month")
        start, next_month = _month_bounds(month_str)

        expenses = (Expense.query
                    .filter(Expense.date >= start, Expense.date < next_month)
                    .order_by(Expense.date.desc(), Expense.id.desc())
                    .all())

        total = sum(e.amount for e in expenses)
        return render_template("index.html",
                               expenses=expenses,
                               categories=CATEGORIES,
                               selected_month=(month_str or date.today().strftime("%Y-%m")),
                               total=total,
                               today=date.today().isoformat())  # 👈 added

    @app.route("/add", methods=["POST"])
    def add():
        amount = request.form.get("amount", type=float)
        category = request.form.get("category")
        description = request.form.get("description")
        dt_str = request.form.get("date")  # YYYY-MM-DD

        # basic validation
        if amount is None or amount <= 0 or not category:
            return redirect(url_for("index"))

        try:
            exp_date = datetime.strptime(dt_str, "%Y-%m-%d").date() if dt_str else date.today()
        except Exception:
            exp_date = date.today()

        expense = Expense(amount=amount, category=category, description=description, date=exp_date)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for("index", month=exp_date.strftime("%Y-%m")))

    @app.route("/delete/<int:expense_id>", methods=["GET"])
    def delete(expense_id):
        exp = Expense.query.get_or_404(expense_id)
        month_str = exp.date.strftime("%Y-%m")
        db.session.delete(exp)
        db.session.commit()
        return redirect(url_for("index", month=month_str))

    @app.route("/report", methods=["GET"])
    def report():
        # Same month filter as index
        month_str = request.args.get("month")
        start, next_month = _month_bounds(month_str)

        # Category totals for pie chart
        rows = (db.session.query(Expense.category, func.sum(Expense.amount))
                .filter(Expense.date >= start, Expense.date < next_month)
                .group_by(Expense.category)
                .all())
        labels = [r[0] for r in rows]
        values = [round(float(r[1]), 2) for r in rows]

        # Daily totals for line chart
        daily_rows = (db.session.query(Expense.date, func.sum(Expense.amount))
                      .filter(Expense.date >= start, Expense.date < next_month)
                      .group_by(Expense.date)
                      .order_by(Expense.date)
                      .all())
        daily_labels = [d[0].strftime("%Y-%m-%d") for d in daily_rows]
        daily_values = [round(float(d[1]), 2) for d in daily_rows]

        selected_month = (month_str or date.today().strftime("%Y-%m"))
        return render_template("report.html",
                               labels=labels, values=values,
                               daily_labels=daily_labels, daily_values=daily_values,
                               selected_month=selected_month)
