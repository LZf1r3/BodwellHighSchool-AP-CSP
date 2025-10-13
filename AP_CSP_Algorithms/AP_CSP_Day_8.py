
"""Write a segment of code that prints out a sequence of random numbers from 1 to 100. Stop once exactly 5 prime numbers have been rpinted.
Note that, we don't know how many iterations we need to get prime numbers. THis is a indefinite loop. It's better to use a while loop."""
import random
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_random_primes():
    prime_count = 0
    while prime_count < 5:
        num = random.randint(1, 100)
        if is_prime(num):
            print(num)
            prime_count += 1

if __name__ == "__main__":
    print_random_primes()