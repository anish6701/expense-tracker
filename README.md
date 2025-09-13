📊 Expense Tracker (SQLite + Python)

🚀 Overview

A simple command-line expense tracker built with Python and SQLAlchemy (SQLite).
You can add daily expenses, view them, and get a quick monthly summary — all stored in a lightweight SQLite database.

This project is designed to:
  
  1. Show logical problem-solving skills in Python.
  2. Demonstrate database handling with SQLAlchemy ORM.
  3. Provide a solid base to later extend into a FastAPI web application.

🛠️ Features

  1. ➕ Add new expenses (amount, category, note, date).
  2. 📋 View all expenses (sorted by date).
  3. 📅 Monthly summary (total spent in a given month).
  4. 🗄️ SQLite database storage (portable, single file).
  5. 💡 Simple CLI interface.

▶️ How to Run

1. Clone the repo

git clone https://github.com/anish6701/expense-tracker.git
cd expense-tracker-sqlite

2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate  # mac/linux

3. Install dependencies

pip install -r requirements.txt

4. Run the tracker

python main.py

📸 Example Run

Expense Tracker
1) Add expense
2) View expenses
3) Monthly total
4) Exit
Choose: 1
Amount: 200
Category: Food
Note: Lunch

✅ Added.

Choose: 2

1   2025-09-13   Food   ₹200.0   Lunch
