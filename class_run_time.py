class Student:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add

    def introduce(self):
        print("Mera naam", self.name, "hai", "meri umar", self.age, "apka address", self.add, "hain")

# Ab user se details lo
naam = input("Aapka naam kya hai? ")
umar = int(input("Aapki umar kya hai? "))
pta = input("apka pta kya hai? ")

student1 = Student(naam, umar, pta)
student1.introduce()