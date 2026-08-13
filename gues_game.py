import random

secret_number = random.randint(1, 10)   # 1 se 10 ke beech random number
attempts = 0

guess = int(input("1 se 10 ke beech ek number guess karo: "))
attempts = attempts + 1

while guess != secret_number:
    if guess > secret_number:
        print("Bahut zyada hai! Chhota number try karo")
    else:
        print("Bahut kam hai! Bada number try karo")
    guess = int(input("Phir se try karo: "))
    attempts = attempts + 1

print("Badhai ho! Aapne sahi guess kiya!")
print("Aapko total", attempts, "attempts lage")