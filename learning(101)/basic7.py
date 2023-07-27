# loops

for i in range(10):
    print(i , end='|')

print()
start =2
stop = 10
step = 2

#step acts as a increment by 

for (i) in range(start,stop,step):
    print(i) 

# loop through list 

alist = [1,2 , True,3,4,5,6,7,8]

for i in alist:
    print(i , end='|')

print()

# using len for accesing index 

for i in range(len(alist)):
     print(alist[i] ,'ji', end='| '  , )

# enumerate for accesing both index and element 

for i,el in enumerate(alist):
    print(i , el)

# sliced 
 # works on both list and tuples
# sliced also get 3 values as params start : stop :  step
blist = [1,2,3,1,2,3,12,3,4]
newslice = blist[start : stop : step]

print(newslice)

# reverse a list using slice

reversed = blist[::-1]
print(reversed)