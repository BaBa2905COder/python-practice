import random

computer = ["stone","paper","scissors"]

secret_number = random.choice(computer)   # 1 se 10 ke beech random number

guess = input("Doremon game ke liye koi select kro stone, paper, scissors me se  ek  guess karo: ")

print("computer ka select ",secret_number)

if secret_number == guess:
    print("no winner")
else:
    print("pta kro apne computer ne kya select kiya")

import random

computer = ["stone", "paper", "scissors"]
secret_number = random.choice(computer)
guess = input("Stone, paper, ya scissors mein se ek choose karo: ")

print("Computer ne choose kiya:", secret_number)

if secret_number == guess:
    print("Tie ho gaya! Dono ne same select kiya")
else:
    print("Alag select kiya — winner decide karna abhi baaki hai")  