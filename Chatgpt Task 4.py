# A number is called a palindrome if it reads the same forward and backward.

rev = 0 
n = int(input("Enter the number to check either it is palindrome or not: "))
a = n # to compare the orignal number seperately for the orignal
while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
if a == rev:
    print("Given number is palindrome")
else:
    print("Given number is not a palindrome")
