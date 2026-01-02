# Write a Python program that takes a positive integer and returns its reverse.

b = 0 
n = int(input("Enter the number to get its reverse: "))
while n > 0:
    a = n % 10
    b = b * 10 + a
    n = n // 10
print(b)

