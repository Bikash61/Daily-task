from collections import Counter, defaultdict, OrderedDict
lst = [1,2,2,3,4,4,3,4,5,5,5,6,5,7,6,7]
print(Counter(lst))

print('-'*30)
d = defaultdict(int)
d['a'] +=5
print(d)
print('-'*30)
d = OrderedDict()
d['one'] = 1
d['two'] = 2

print(d)

