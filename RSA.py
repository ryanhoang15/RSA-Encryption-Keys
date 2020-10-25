# Goal: Generate vaild keys: e, n
# 1. chose 2 random prime #s (p,q):
# 2. n = pq
# 3. find another random int e
# gcd(e,(p-1)(q-1)) = 1 e and (p-1)(q-1) are relative prime
# import random
# random.randint(a,b) => random int between a,b
# Mersenne primes: 2^x - 1 is usually prime
# 1 => 2^1 - 1 = 1
# x = 2 => 2^2 - 1 = 3
# maybe use trail division to check if # is prime

import random
import math


# this function is generating 2 random numbers for p and q and checking if it is prime or not
# it is also getting a random value for e and checking if it is prime or not
# than e and p-1 * q-1 is getting passed to a function to see it the gcd is 1
def Main():
    p = random.randint(2, 201)
    q = random.randint(2, 201)
    e = random.randint(2, 20)

    ePrime = checkPrime(e)
    isPrime = checkPrime(p)
    isPrime_2 = checkPrime(q)

    while True:
        while not isPrime or not isPrime_2 or not ePrime:
            if not checkPrime(p):
                p = random.randint(2, 201)
                isPrime = checkPrime(p)

            elif not checkPrime(q):
                q = random.randint(2, 201)
                isPrime_2 = checkPrime(q)

            else:
                e = random.randint(2, 20)
                ePrime = checkPrime(e)

        n = p * q

        valid = gcd(e, (p - 1) * (q - 1))

        if valid == 1:
            print("Valid keys:", e, ",", n)
            print("p", p)
            print("q", q)
            break
        else:
            print("Not relatively prime")
            print("Getting a new e")
            e = random.randint(2, 20)
            ePrime = checkPrime(e)


# this function is checking if a number is prime or not
def checkPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


# this function is calculating the gcd
def gcd(num1, num2):
    # formula a = bq + r
    a = num1
    b = num2
    if num1 < num2:
        a = num2
        b = num1

    remainder = 0
    while b > 0:
        remainder = a % b
        a = b
        b = remainder

    return a


Main()
