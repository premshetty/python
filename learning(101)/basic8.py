#sets nd dict

#dict

x = {'A':1,'b' : 2 , "c" : 3}
x['d0'] = 0
del x['b']
print(x)

print(list(x.keys()))
print(list(x.values()))


# print key and values of a dict

for key,value in x.items():
    print(key,value)


# another way

for key in x:
    print(key , x[key])


# sets


a = set()
c ={1,2,3,4,5,1,2,3}
a.add(5)
b = {6}
b.add(7)
print(a)
print(b)

print(3 in c)
