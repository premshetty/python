# comprehensions

# create list 
x= [0 for x in range(5)]
a = [a+1 for a in range(5)]

b = [[b for b in range(100)] for b in range(5) ]

print(a , x)

print(b)

d = [d for d in range(100) if d%5==0]
print(d)


# dict

f = {f:f for f in range(100) if f%3==0}

print(f)


# set


g = {g for g in range(100) if g%3==0}

print(g)

# tuple
h = tuple(h for h in range(100) if h%3==0)

print(h)