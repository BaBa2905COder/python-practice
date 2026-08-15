import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT, age INT, city TEXT)"
)

#data dal gay hn 

#cursor.execute(
 #   "INSERT INTO student (id, name, age, city) VALUES (101, 'Shahil', 25, 'Ludhiana')"
#)

# Naya student add kiya - YAHAN
#cursor.execute(
 #   "INSERT INTO student (id, name, age, city) VALUES (102, 'Anjali', 23, 'Delhi')"
#)

# ek Naya student add kiya - YAHAN
#cursor.execute(
#    "INSERT INTO student (id, name, age, city) VALUES (103, 'Sanskar', 22, 'Kanpur')"
#)

#connection.commit()

# Ab data ko dikhao

cursor.execute("SELECT * FROM student")

#SELECT * FROM student WHERE city = 'Delhi';


#cursor.execute(" SELECT * FROM student WHERE city = 'Delhi'")

cursor.execute("SELECT * FROM student WHERE age = 25")

result = cursor.fetchall()


print(result)

connection.close()
