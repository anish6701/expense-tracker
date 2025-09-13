# app/tracker.py
from contextlib import contextmanager
from .database import SessionLocal, init_db
from . import crud
import datetime

init_db()   # ensure tables exist when module is imported

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ExpenseTracker:
    def add_expense(self, amount, category, note=None, date=None):
        with get_db() as db:
            return crud.create_expense(db, amount, category, note, date)

    def view_expenses(self):
        with get_db() as db:
            return crud.list_expenses(db)

    def monthly_summary(self, year_month=None):
        if year_month is None:
            year_month = datetime.date.today().strftime("%Y-%m")
        with get_db() as db:
            return crud.monthly_total(db, year_month)
