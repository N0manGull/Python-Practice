# An Armstrong number (for 3-digit numbers) is a number such that:

# The sum of the cubes of its digits is equal to the number itself.

n = int(input("Enter a 3 digit number to check either it is Armstrong or not: "))
orignal = n
c = 0
while (n>0):
    a = n % 10
    b = a*a*a
    c = c + b
    n = n // 10
    print(c)
if (c == orignal):
    print("No. is Armstrong")
else:
    print("Not an Armstrong Number")
    
# To improve:
# Rename c → total (readability)

# Remove print(c) (debug statement)

# Handle non-3-digit numbers gracefully