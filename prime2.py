def is_prime(num):
    is_it_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_it_prime = False
    
    if is_it_prime:
        print("Ye number prime hai")
    else:
        print("Ye number prime nahi hai")

number = int(input("Number batao jiska pata karna hai prime hai ki nahi: "))
is_prime(number)