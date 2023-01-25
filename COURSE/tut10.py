print("TUTORIAL 10\n\n")

# 10.0FUNCTIONS

# Builtin Function
a = 10
b = 15
c = sum((a,b))
print(c,"\n\n")

# User-Defined Function

def funcY():
    print("DAYUMmm!")
v= funcY() # although runs the func but stores 'return' value
funcY() # using/invoking function

print('\n\n')

# Ques: make a AVERAGE function with docstring
def avg(a,b):
    """This function returns average value
of only two variables taken as parameters"""
    return (a+b)/2
x=10
y=15
av=(avg(x,y))
print(av) #average value through invoking
print(avg.__doc__) # func to print docstring

