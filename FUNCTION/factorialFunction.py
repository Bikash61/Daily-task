
#WAP to caluclate the factorial of n number 
a = int(input("Enter the number you want to print?"))

def factorial(a, fact = 1):
    for i in range(1, a+1):
        fact*=i
    print(fact)

factorial(a)


