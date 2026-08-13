class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Mera naam", self.name, "hai" , "meri umar", self.age)

student1 = Student("Rohan", 20)
student1.introduce()