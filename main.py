#1: Create a program that gets the expenses and income
#2: Add Date column
#3: Raise an input error if the user inputs anything other than "expense" or "income"
#4: Raise an input error if the user inputs an invalid date format
#5: Raise a type error if user inputs a non-integer amount
#6: Sort by date and display the total expenses and income for the desired month

from datetime import datetime as dt
import sqlite3

database= sqlite3.connect("expense.sqlite")
cursor= database.cursor()
cursor.execute('DROP TABLE IF EXISTS "August"')
cursor.execute("""
     CREATE TABLE IF NOT EXISTS "2026"(
        Type TEXT,
        Amount INTEGER,
        Date TEXT
    )
""")
while True:
    while True:
        type= input ("expense or income?")
        if type in ("expense", "income"):
            break
        else:
            print("Invalid input. Please enter exactly 'expense' or 'income'.")
            continue
    while True:
        amount_str= input ("how much?")
        try:
            amount= int(amount_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer amount.")
    while True:
        date= input ("date? (YYYY-MM-DD)")
        try:
            dt.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
    cursor.execute("""
        INSERT INTO "2026"(Type, Amount, Date) VALUES(?, ?, ?)
    """, (type, amount, date))
    another= input ("add another?y/n")
    database.commit()
    if another == "n":
        break