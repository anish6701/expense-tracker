# main.py
from app.tracker import ExpenseTracker

def main():
    t = ExpenseTracker()
    while True:
        print("\nExpense Tracker")
        print("1) Add expense")
        print("2) View expenses")
        print("3) Monthly total")
        print("4) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            amt = float(input("Amount: ").strip())
            cat = input("Category: ").strip()
            note = input("Note (optional): ").strip()
            t.add_expense(amt, cat, note or None)
            print("✅ Added.")
        elif choice == "2":
            rows = t.view_expenses()
            for r in rows:
                print(f"{r.id}\t{r.date}\t{r.category}\t₹{r.amount}\t{r.note}")
        elif choice == "3":
            total = t.monthly_summary()
            print("Monthly total:", total)
        elif choice == "4":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
