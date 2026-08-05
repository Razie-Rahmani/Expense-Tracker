#1: Create a program that gets the expenses and income
#2: Add Date column
#3: Raise an input error if the user inputs anything other than "expense" or "income"
#4: Raise an input error if the user inputs an invalid date format
#5: Raise a type error if user inputs a non-integer amount
#6: Fetch stored data from the database and display it in a table format
#7: Sort by date and display the total expenses and income for the desired month

from datetime import datetime as dt
import sqlite3
from sqlite3 import Row

database= sqlite3.connect("expense.sqlite")
cursor= database.cursor()
database.row_factory= sqlite3.Row
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Year_2026(
        ID INTEGER PRIMARY KEY,
        Type TEXT,
        Amount INTEGER,
        Date TEXT
    )
""")

def add_row():
    while True:
        transaction_type= input ("expense or income?")
        if transaction_type in ("expense", "income"):
            break
        else:
            print("Invalid input. Please enter exactly 'expense' or 'income'.")
            continue
    while True:
        transaction_amount= input("How much?\n\n(Absolute Value)")
        try:
            amount= int(transaction_amount)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer amount.")
            continue
    while True:
        transaction_date= input("What date?\n\n(YYYY-MM-DD)")
        try:
            dt.strptime(transaction_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
    cursor.execute("""
        INSERT INTO Year_2026(Type, Amount, Date) VALUES(?, ?, ?)
        """, (transaction_type, amount, transaction_date))
    database.commit()


def edit_row():
    pass

def delete_row():
    pass

def sort():
    pass

def show_table():
    pass

while True:
    user_request= input("What would you like to do?\n\nAdd, Edit, Delete, Sort, Show Table [Case Sensitive]")
    if user_request== "Add":
        add_row()
    elif user_request== "Edit":
        edit_row()
    elif user_request== "Delete":
        delete_row()
    elif user_request== "Sort":
        sort()
    elif user_request== "Show Table":
        show_table()