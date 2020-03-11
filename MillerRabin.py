#-*- coding: utf8 -*-

import random

"""
Explanation:
To check an odd number larger than 1 is prime or not, we follow these step:
1. Convert n -1 to 2^s * d (s,d are integer; d is odd)
2. Check number a in range [2, min(n-1, ⌊2(lnn)^2⌋)]
   If a^d ≢ 1 (mod n) and (a^d)^(2^r) ≢ -1 (mod n) with r in range(0, s- 1),
   n is not prime
3. If n pass all the trials with number a, n is prime
"""


lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
            59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
            127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
            191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
            257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
            331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
            401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
            467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
            563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
            631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
            709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
            797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
            877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953,
            967, 971, 977, 983, 991, 997]


def isPrime(num):
    # Function check prime in two cases:
    # Low primes: a list of given numbers in lowPrimes
    # Big primes: check using millerCheck function
    if num < 2:
        return False
    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if num % prime == 0:
            return False
    return millerCheck(num)


#Check big prime numbers
def millerCheck(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t = t + 1

    #Falsify num's primality 5 times
    time = 0
    while time != 5:
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                     i = i + 1
                     v = (v ** 2) % num
        time = time + 1
    return True


def generateLargePrime(keysize = 1024):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if isPrime(num):
            return num


if __name__ == '__main__':
    print('==== Rabin Miller prime number Program ====')
    print('Press 1 to check prime number')
    print('Press 2 to generate a big size prime number')
    print('Press 3 to exit')
    while(1):
        choice = input('\n 1. Check prime \n 2. Big size prime number \n 3. Exit\n')
        if choice == 1:
            input_number = input('Enter a number: ')
            if isPrime(input_number):
                print('Input is prime')
            else:
                print('Input is not prime')
        elif choice == 2:
            keysize = input('Enter keysize: ')
            print(generateLargePrime(keysize))
        elif choice == 3:
            exit()
        else:
            print('Choose correct choice: ')