# count é um iterador sem fim

from itertools import count

c0 = count(10) # começa no 10
r0 = range(10) # vai ate 10
c1 = count(10, 8) 
r1 = range(10, 100, 8)
c2 = count(step = 8, start = 8)


# print(next(c1))
# print(next(c1))
# print(next(c1))
# print(next(c1))
# print(c1)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))


for i in c1:
    if i > 100:
        break
    print(i)
    
print()
print('range')
print()

for i in r1:
    if i > 100:
        break
    print(i)