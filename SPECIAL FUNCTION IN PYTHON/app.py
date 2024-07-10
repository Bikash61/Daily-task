#Zip Function

lst1 = ['Bikash','Samir', 'Pragya']
lst2 = [20,23,19]

print(list(zip(lst1,lst2)))

print('-'*30)

Matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(Matrix)])
print([list(row) for row in zip(*Matrix)])
print([list(row) for row in zip(*[list(row) for row in zip(*Matrix)])])

print('-'*30)

lst1 = [2,3,5]
lst2 = [3,4,6]

lst = zip(lst1,lst2)

print([i*j for i,j in lst])
print(sum([i*j for i,j in zip(lst1,lst2)]))

#Filter Function 
print('-'*30)
num = [1,3,4,5,3,5,3,5345,34,4,3,5,3,5,4534,756,867,956,56,98]
def is_even(n):
    if n%2==0:
        return True
    else:
        return False

print(list(filter(is_even,num)))

print('-'*30)
#Lambda Function

mul_num = lambda x,y:x*y
print(mul_num(56,67))

print('-'*30)

lst0 = [1,2,3,4,5,6,7,8]
print(list(filter(lambda x: x%2==0,lst0)))
print('-'*30)

#Map Function
map_use = [1,2,3,4,5,6,7,8,9]

def srq(x):
    return x**2

print(list(map(srq,map_use)))
#Printing using lambda 
print(list(map(lambda x: x**2,[2,4,6,7])))
   
print('-'*30)

names = ['Bikash', 'Chandan', 'Manish', "Hari"]
print(list(map(lambda x: len(x),names)))