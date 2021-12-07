def prime_check(number):
    prime = True
    for n in range(2, number):
        modulus_value = number % n
        if modulus_value == 0:
            prime = False
            break
    if prime:
        print("%d is a prime number" % number)
    else:
        print("%d is not a prime number" % number)

prime_check(11)