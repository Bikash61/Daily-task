
#First method
a = int(input("Enter the dollar you want to convert in INR"))
print("$", a)
def conversion( a):
    a = a*83.6
    print("INR",a)
conversion(a)


#Second Method 
def converter (usd):
    inr = usd *83.6
    print("$", usd, "is equal to", "INR", inr  )


converter(3)