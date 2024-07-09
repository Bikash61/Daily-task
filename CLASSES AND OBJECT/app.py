class greet:
    print("Hello Everyone")

greet()

print('-'*40)

class person:
    name = "Bikash"
    age = 20
    Rollno = 11222899

details = person()

def print_details():
    print("Name: ",details.name)
    print("Age: ",details.age)
    print("Roll No: ",details.Rollno)

print_details()

print('-'*40)

#changing the value of an object

details.name = "Hashim"
details.age = 29
details.Rollno = 1117234

print_details()
