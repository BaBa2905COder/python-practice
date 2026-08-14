import sqlite3

# step - 1 :  connect kro

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

# step - 2 : SQL Commands chalao

#cursor.execute("Yaha Apna SQL Commnad likhan hota hai")


# step - 3 : (Agr Data cahnge kiya ho jese - insert/update/delete) : save krene ke liye     

connection.commit()

# step - 4 : (Agr Data dekhna ho to - SELECT ): result nikalo 

result = cursor.fetchall()

print(result)

# step - 5 : connection band kro 

connection.close()