print("EXERCISE 2:\nCalculator")

# BEGIN:

# Version 1.0
print("_____BASIC arithmatic CALCULATOR____\nEnter equation:\n")

n = float(input())
e = input()
n1 = float(input())
if e == '+':
    print(n+n1)
elif e == '-':
    print(n-n1)
elif e == 'x':
    print(n*n1)
elif e == '/':
    print(n/n1)
elif e == '^':
    print(n**n1)
else :
    print("--Syntax Error--") 

# Version 2.0
print("\n\n_____BASIC arithmatic CALCULATOR____\n(Version 2.0)\n\nEnter equation:\n")
eq = input()
try:
    el = eq.split('+')
    print(float(el[0])+float(el[1]))
except:
    pass
try:
    el = eq.split('*')
    print(float(el[0])*float(el[1]))
except:
    pass
try:
    el = eq.split('-')
    print(float(el[0])-float(el[1]))
except:
    pass
try:
    el = eq.split('^')
    print(float(el[0])**float(el[1]))
except:
    pass
try:
    el = eq.split('/')
    print(float(el[0])/float(el[1]))
except:
    pass


