import sqlite3

# Database se connect kro 
# (agar file nhi hai, toh naya ban jayega)

connection = sqlite3.connect("student.db") 


# Ek "cursor" banao - ye SQL commands ke liye 

cursor = connection.cursor()

# Table banao

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
    )
""")

#changes ko save kro

connection.commit

print("table bn gya")
