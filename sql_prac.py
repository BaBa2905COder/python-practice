
import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT, age INT, city TEXT)"
)



connection.commit()

cursor.execute("SELECT * FROM student WHERE age >= 22")
result = cursor.fetchall()
print(result)

cursor.execute("SELECT * FROM student WHERE city = 'Ludhiana'")
result = cursor.fetchall()
print("All students:", result)


cursor.execute("UPDATE student SET city = 'Chandigarh' WHERE id = 101")
connection.commit()   # yaad rakho - commit karna zaroori hai, warna save nahi hoga


cursor.execute("SELECT * FROM student")
result = cursor.fetchall()
print("final output", result)


cursor.execute("DELETE FROM student WHERE id = 103")
connection.commit()

cursor.execute("SELECT * FROM student")
result = cursor.fetchall()
print("After delete:", result)

connection.close()
