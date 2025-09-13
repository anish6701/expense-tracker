# app/crud.py
import datetime
from sqlalchemy import func
from .models import Expense

def create_expense(db, amount: float, category: str, note: str | None = None, date: datetime.date | None = None):
    if date is None:
        date = datetime.date.today()
    expense = Expense(amount=amount, category=category, note=note, date=date)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def list_expenses(db):
    return db.query(Expense).order_by(Expense.date.desc()).all()

def monthly_total(db, year_month: str):
    # year_month example: "2025-09" -> uses SQLite strftime to compare YYYY-MM
    total = db.query(func.sum(Expense.amount)).filter(
        func.strftime("%Y-%m", Expense.date) == year_month
    ).scalar()
    return total or 0.0
