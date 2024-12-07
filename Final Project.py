total_income = 0
total_expenses = 0

def add_income(total_income):
    try:
        amount = float(input("Enter income amount"))
        total_income += amount
        print(f"Added income: ${amount:.2f}") # the .2 thingy rounds up the number to 2 decimal places. convient to make it look neat
    except ValueError:
        print("Please enter a valid number.")
    return total_income

def add_expense(total_expenses):
    try:
        amount = float(input("Enter expense amount: "))
        total_expenses += amount 
        print(f"Added expense: ${amount:.2f}")
    except ValueError:
        print("Please enter a valid number.")
    return total_expenses


def summary(total_income, total_expenses):
    remaining = total_income - total_expenses
    print("\n ---- Budget Summary ----")  #\n mean to go to the next line and continue the setence
    print(f"Total Income: ${total_income: .2f}")
    print(f"Total Expenses: ${total_expenses: .2f}")
    print(f"Remaining balance: ${remaining: .2f}")
    print("---------------------------")

