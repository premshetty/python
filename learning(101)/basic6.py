# list and tuples

# tuples, immutable

x = (0,1,2,3,4)
print(x[0]) 

# list , mutable

a = [1,2,'gh', True]

# make a deep copy
b = a[:]
print(a[1])
print(len(a))
a.extend([1,2,3,4,'e',5])
print(a.pop())
print(a.remove(2))
print(a)

print(a.clear())
print(a)

print(b)


