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