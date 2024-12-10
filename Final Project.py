#GraphiBucksssss

from tkinter import *


total_income = 0
total_expenses = 0

def add_income():
    global total_income
    try:
       amount = float(income_entry.get()) #this will get the info from user
       total_income +=amount
       result.config(text=f"Added income: ${amount: .2f}")  # to make it look neater, showing the value with 2 decimal places. this is especially for displaying currency.
       income_entry.delete(0, END) # this will clear out the widget/box
    except ValueError:
        result.config(text="Please enter valid numbers.")

def add_expense():
    global total_expenses
    try:
        amount = float(expense_entry.get()) #this will get the info from user
        total_expenses +=amount
        result.config(text=f"Added expense: ${amount: .2f}")
        expense_entry.delete(0, END) # this will clear out the widget/box
    except ValueError:
        result.config(text="Please enter valid numbers.")

def show_summary():
    remaining = total_income - total_expenses
    result.config(text=f"Income: ${total_income: .2f}, Expenses: ${total_expenses: .2f}, Balance: ${remaining: .2f}")

window = Tk()
window.geometry("500x500")  # to make the block of the pop-up window bigger
window.title("Graphibucks") # to make it named GraphiBucks

window.config(background="grey") #my hair after this project is done lol

label = Label(window, text="Hello! Need help with money? I got you!")
label.pack() # so that the line above can go into effect

#Making me rip my hair off

Label(window, text="Added Income:").pack(pady=5) #pady is to make it look nicer by moving it on the y-coordinate
income_entry = Entry(window)
income_entry.pack(pady=5)
Button(window, text="Add Income", command=add_income).pack(pady=5)

Label(window, text="Added Expense:").pack(pady=6) 
expense_entry = Entry(window)
expense_entry.pack(pady=6)
Button(window, text="Add Expense", command=add_expense).pack(pady=6)

Button(window, text="Show Me My Money", command=show_summary).pack()

# Incomelabel = Label(window, text="Added Income: ").grid(row=0, column=0)
# IncomeEntry = Entry(window).gride(row=0,column=1)

result = Label(window, text="")
result.pack()

window.mainloop()

#omg> i js made my own project?????? This was lowkey fun