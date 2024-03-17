
#WAP to print odd number till any number by using recursive function
# def odd_number(n):
#     if (n<10):
#         if (n %2 != 0):
#             print(n)
#         odd_number(n+1)
# odd_number(1)
    
#Write a program to print the even number till 20 using recursive function 

def even_number(m):
    if(m<=20):
        if(m%2 ==0):
            print(m)
        even_number(m+1)
even_number(1)


