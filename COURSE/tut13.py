print("TUTORIAL 13\n\n")

# 13.1 SCOPE of VARIABLES and GLOBAL keyword

l = 10 # GLOBAL variable ie. scope till limits of whole program

def fun(n): # here inside GLOBAL var acts as read only variable (can't be altered)
    l = 5 # LOCAL variable ie. scope till the limits of FUNCTION
    m = 10
    print(l, m) # here it first checks LOCAL scope ie. present here
    print(n, "DONE!")
def fun2():
    global l # now GLOBAL variable can be HANDLED
    l +=10
    print(l)

fun("Its")
fun2()

print(l) # here GLOBAL var is printed coz LOCAL is out of scope
#print(m) # will not execute coz 'm' is out of scope ie. its LOCAL


# 13.2 NESTED functions
x = 0
def outer(n):
    x = n
    def inner():
        global x
        x += 10 # goes out of whole outer func. to check for GLOBAL var.
    print("after OUTER:", x)
    inner()
    print("after INNER:", x)

outer(25)
print("changed value due to INNER:", x)