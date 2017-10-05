# -*- coding: utf-8 -*-
from collections import Iterable,Iterator
def g():
    yield 1
    yield 2
    yield 3
print('Iterable? [1,2,3]:',isinstance([1,2,3],Iterable))
print('Iterable?\'ABC\':',isinstance('ABC',Iterable))
print('Iterable? 123:',isinstance(123,Iterable))
print('Iterable? g():',isinstance(g(),Iterable))

print('Iterable? [1,2,3]:',isinstance([1,2,3],Iterator))
print('Iterable?\'ABC\':',isinstance('ABC',Iterator))
print('Iterable? 123:',isinstance(123,Iterator))
print('Iterable? g():',isinstance(g(),Iterator))

# iter list
print('for x in [1,2,3,4,5]:')
for x in [1,2,3,4,5]:
    print(x)
print('for x in iter([1,2,3,4,5])')
for x in iter([1,2,3,4,5]):
    print(x)
	
print('next()')
it = iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a':1,'b':2,'c':3}
print('iter key',d)
for k in d.keys():
    print('key:',k)

print('iter key',d)
for v in d.values():
    print('values:',v)

#iter both key and values
print('iter key and value')
for k,v in d.items():
    print('item:',k,v)

#iter list with index
print('iter enumerate([\'a\',\'b\',\'c\'])')
for i,v in enumerate(['a','b','c']):
    print(i,v)
	
#iter complex list
print('iter[(1,2),(2,3),(3,4)]')
for x,y in [(1,2),(2,3),(3,4)]:
    print(x,y)
	print (x,y)
	print(x,y)
	print (x,y)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	