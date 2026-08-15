import sqlite3

def connect_db():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            course TEXT)"""
    )

    connection.commit()
    return connection, cursor


def add_student(cursor, connection):
    name = input("Student Ka Naam Batao !")
    age =  int(input("Student Ki Age Batao !"))
    course = input("Student Ke Course Ka Naam Batao !")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    connection.commit()
    print("Student Successfully Add Ho Gya Hai !")

def view_student(cursor):
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()

    if len(all_students) == 0:
        print("Koi Student Nahi Mila !!!")
    else:
        print("\n --- Sabhi Students ---")

        for student in all_students:
            print(
                "ID:", student[0], "| Naam:", student[1], "| Umar:", student[2], "| Course:", student[3]
            )


def search_student(cursor):
    search_name = input("Kis Student Ko Dhoodnna Hai (Naam Batao) !")
    search_course = input("Kis Course Se Dhoodnna Hai (Course Batao)!")

    cursor.execute("SELECT * FROM students WHERE name = ? OR course = ?", (search_name, search_course))
    result = cursor.fetchall()

    if len(result) == 0:
        print("Ye Student Nahi Mila !")
    else:
        for student in result:
            print(
                "ID:", student[0], "| Naam:", student[1], "| Umar:", student[2], "| Course:", student[3]
            )

def update_student(cursor, connection):
    student_id = int(input("Kis Student Ka ID Update Karna Hai !"))

    new_course = input("Naya Course Batao: ")

    new_name = input("Naya name Batao: ")

    new_age = input("Naya age Batao: ")
    

    cursor.execute("UPDATE students SET course = ?, name = ?, age = ? WHERE id = ? ", (new_course, new_name, new_age, student_id))
    connection.commit()

    if cursor.rowcount == 0:
        print(" Ye ID Nhi Mila !!")
    else:
        print("Student Update Ho Gaya !")


def delete_student(cursor, connection):
    student_id = int(input("Kiss Student Ka ID Delete Karna Hai:"))

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()

    if cursor.rowcount == 0:
        print("Ye ID Nhi Mila !")
    else:
        print("Student Delete Ho Gya! Hai!")


def menu():
    connection, cursor = connect_db()
    while True:
        print("\n --- Student Management System ---")
        print("1. Naya Student ADD Karo !")
        print("2. Sab Student dikhao  !")
        print("3. Student SEARCH    Karo !")
        print("4. Student UPDATE Karo !")
        print("5. Student DELETE Karo !")
        print("6. EXIT Karo !")

        choice = input("Apna Choice Number Daalo !")

        if choice == "1":
            add_student(cursor, connection)
        elif choice == "2":
            view_student(cursor)
        elif choice == "3":
            search_student(cursor)
        elif choice == "4":
            update_student(cursor, connection)
        elif choice == "5":
            delete_student(cursor, connection)
        elif choice == "6":
            print("Dhanyabaad ! Program band Ho gaya !")
            connection.close()
            break
        else:
            print("Galat ! choice kiya hn 1-6 ke bich ka select kro !--")

menu()