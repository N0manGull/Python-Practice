# A prime number is a number greater than 1 that has only two divisors:

import math                 # Import math module to use sqrt() function

n = int(input("Enter the number to check either it is prime or not: "))
   

if n <= 1:
    print("Not a Prime Number")
else:
    a = 2
    while(a <= math.isqrt(n)): # math.sqrt(n) returns a float but math.isqrt(n) returns an integer 
        if (n % a == 0):
            print("Not a Prime Number")
            break
        a += 1
    else:
        print("Prime Number")
    