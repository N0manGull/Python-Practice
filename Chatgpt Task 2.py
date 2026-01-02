# Write a function that takes a positive integer and returns how many digits it has.

count = 0
n = int(input("Enter a number to count the total number of digits: "))

if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10     # same as n = n // 10
        count += 1   # same as count = count + 1
print(count)
