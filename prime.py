number = int(input("Number batao jiska pata karna hai prime hai ki nahi: "))

count = 0

for i in range(2, number):
    if number % i == 0:
        count = count + 1

if count == 0:
    print("Ye number prime hai")
else:
    print("Ye number prime nahi hai")



def check_prime(number):
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count = count + 1
    if count == 0:
        print("Ye number prime hai")
    else:
        print("Ye number prime nahi hai")

number = int(input("Number batao jiska pata karna hai prime hai ki nahi: "))
check_prime(number)