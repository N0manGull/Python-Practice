# Write a Python function that takes a positive integer and returns the sum of its digits.

sum = 0
n = int(input("Enter the number to get its each number's sum: "))
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print(sum)
