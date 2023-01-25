print("TUTORIAL 15\n\n")

# 15.1 LAMBDA or ANONYMOUS functions
"""
Shorthand for declaring functions
"""

# ADD function (normal way)

def add(x,y):
    return x+y
print(add(10,5))

# MINUS function (LAMBDA way)

minus = lambda x,y: x-y
print(minus(10,5))

# 15.2 Using LAMBDA with SORT function
def first(a):
    return a[1]
a = [['i',3],['e',2],['o',4],['e',2],['a',1]]
a.sort(key=first) # Long way
print(a)

#also

a.sort(key=lambda x:x[1]) # Lambda way