print("TUTORIAL 26\n\n")

# 26.1 ITERATION Basics
"""
Iterable  - __iter__() or __getitem__()
Iterator  - __next__() [also, GENERATOR]
Iteration - the whole process
"""
# 26.2 GENERATOR 

def gen(n):
    for i in range(n):
        yield  i# smart way to keep iteration on set  
        # but not to begin with it
g = gen(4) # 0-3
#print(g) # gives location not value 
print(g.__next__()) # begins iteration (0)
print(g.__next__()) # (1)
print(g.__next__()) # (2)
print(g.__next__(),"\n") # (3)

# also

a ="abcdefghijklmnopqrstuvwxyz"
i = iter(a)
print(i.__next__()) # (a)
print(i.__next__()) # (b)
print(i.__next__(),'\n') # (c)

a2 = 1234567890 
i2 = iter(a2) # tells it is ITERABLE or NOT