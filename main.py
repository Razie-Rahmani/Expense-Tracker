#1: Create a program that gets the expenses and income

import sqlite3

database= sqlite3.connect("expense.sqlite")
cursor= database.cursor()
cursor.execute("""
     CREATE TABLE IF NOT EXISTS August(
        Type TEXT,
        Amount INTEGER
    )
""")
while True:
    type= input ("expense or income?")
    amount= int(input ("how much?"))
    cursor.execute("""
        INSERT INTO August(Type, Amount) VALUES(?, ?)
    """, (type, amount))
    another= input ("add another?y/n")
    database.commit()
    if another == "n":
        break