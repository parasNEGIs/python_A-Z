from unicodedata import decimal


print("TUTORIAL 24\n\n")

# 24.0 Python DECORATOR

# Using FUNCTION as VARIABLE
def func():
    print("FUNC hai bhai!!")

func2 = func # func copied not a pointer created
del func # no change in func 2

# Using func as RETURN value
def funret(n):
    if n>0:
        return print
    elif n<0:
        return sum
    else:
        return func
a = funret(2)
print(a)

# Using func as PARAMETER
def exe(func):
    func()

exe(print)

# NESTED functions (dECORATOR)
def paru(func):
    def now():
        print("Executing now....")
        func()
        print("EXECUTED!!!")
    return now

@paru # DECORTOR shortcut
def iam():
    print("PARAS(NEGI)UMRAO")

iam = paru(iam)  # DECORATOR other way

iam()