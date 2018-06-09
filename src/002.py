import numpy as np

def factorial(n):
    if float(n).is_integer():
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        print("func:factorial is only for integers")

if __name__ == "__main__":
    n = int(input("enter a positive integer or zero:"))
    print(factorial(n))
