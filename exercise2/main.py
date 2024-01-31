#Shiven, Jay Lebo, Alec, Andrew, Jay Patel

import time
import random

def fib(n):
    if n <=1:
        return n
    else: 
        return fib(n-1) + fib(n-2)

def main():
    n = random.randint(15, 35)

    start = time.time()
    answer = fib(n)
    end = time.time()

    execution = end - start

    print(f"fib({n}) = {answer}")
    print(f"fib({n}) took {execution}")


main()

