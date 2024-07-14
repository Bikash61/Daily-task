#WAP to check the wheather the program is palindrome or not 

def palindrome(s):
    return s[::-1]
    
    
s=input("Enter the string:")
if s==palindrome(s):
    print("The string is palindrome")
else:
    print("The string is not palindrome")