# 8. Write a function, is_prime, that takes an integer and returns True if 
# the number is prime and False if the number is not prime. 

def is_prime(n):
    if n < 1:
        raise Exception("Please enter a positive integer")

    elif n == 1:
        print("1 is neither prime nor composite")

    else:
        for i in range(2,n):
            if n % i == 0:
                print("Not prime")
                break

        else:
            print("Prime")


is_prime(2)