class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Mera naam", self.name, "hai aur meri umar", self.age, "hai")

Student1 = Student("sahil", 25)
Student2 = Student("vikas",26)
Student3 = Student("sanskar",23)

Student3.introduce()