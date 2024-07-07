#defining list
li = [1,2,3,4,5]
#defining function
def sq_li(li):
    return [i**2 for i in li]
#defining another function
def cu_li(li):
    return [i**3 for i in li]
#defining final function 
def final(li):
    lst1 = sq_li(li)
    lst2 = cu_li(li)
    return [lst1[i] + lst2[i] for i in range(len(lst1))]

result = final(li)
print(result)