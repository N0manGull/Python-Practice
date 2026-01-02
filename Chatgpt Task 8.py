# Write a program that prints a pyramid/triangle number pattern based on user input

n = int(input("Enter the the number to get a number's triangle: "))

if n <= 0:
    print("Enter a positive number!")
else:
    for i in range (1, n + 1):  
        for j in range (1, i + 1):
            print(j, end=" ")
        print()

# In python for loop automatically generate increment but in case of decrement we use this loop:
# Outer loop: rows decreasing from n down to 1
# for i in range(n, 0, -1):
    # Inner loop: numbers from 1 up to current row number
    # for j in range(1, i + 1):
