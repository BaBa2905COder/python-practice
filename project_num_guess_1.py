secret_number = 6  # abhi ke liye fix rakhte hain, baad mein random karenge

guess = int(input("1 se 10 ke beech ek number guess karo: "))

while guess != secret_number:
    if guess > secret_number:
        print("Bahut zyada hai! Chhota number try karo")
    else:
        print("Bahut kam hai! Bada number try karo")
    guess = int(input("Phir se try karo: "))

print("Badhai ho! Aapne sahi guess kiya!")