# // Fibbonacci series till given number:
n = int(input("Enter the number to get Fibonacci series till that number: "))

a = 0
b = 1
if (n<=0):
    print("Fibonacci series does'nt exist in negative values or at zero.")
elif(n>0):
    print(a, b, end=" ")
    while True: #in case of for loop, for _ in range(n):
        c = a + b
        if (c > n):
            break
        print(c, end=" ")  #here end=" " will give space instead of new line in the output
        a, b = b, c #simultanious assignment to update both variables at the same time
    # in this case variable a becomes b and b becomes c at the same time in the same line
        
        