class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        print("Mera naam", self.name, "hai", "mera course", self.course, "hai")

kitne_students = int(input("Kitne students ki details bharni hain? "))

for i in range(kitne_students):
    naam = input("Naam batao: ")
    addmision = input("course batao: ")
    student = Student(naam, addmision)
    student.introduce()


# multiple detail ko ek sath output

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Mera naam", self.name, "hai aur meri umar", self.age, "hai")

# Step 1: Ek khaali list banao jisme sab students store honge
all_students = []

kitne_students = int(input("Kitne students ki details bharni hain? "))

# Step 2: Sirf INPUT lo, abhi output mat dikhao
for i in range(kitne_students):
    naam = input("Naam batao: ")
    umar = int(input("Umar batao: "))
    student = Student(naam, umar)
    all_students.append(student)   # is student ko list mein daal do

# Step 3: Ab jab saari details aa gayi, TAB sabka output dikhao
print("\n--- Sabki Details ---")
for student in all_students:
    student.introduce()