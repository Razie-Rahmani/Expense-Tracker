#1: Create a program that gets the expenses and income

import sqlite3

database= sqlite3.connect("expense.sqlite")
cursor= database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS August(Expenses, Income)")
result= database.execute("SELECT name FROM sqlite_master")
(result.fetchone())