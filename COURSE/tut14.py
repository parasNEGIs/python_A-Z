print("TUTORIAL 14\n\n")

# 14.1  RECURSION
"""
function in the function in itself
"""

# factorial (iterative)

def factIT(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
print("Enter no.")
n= int(input())
print("Factorial via Iterative method:", factIT(n))

# factorial (recursive)

def factREC(n):
    if n==1:
        return 1
    else:
        return n*factREC(n-1)
print("Enter no.")
n2= int(input())
print("Factorial via Recursive method:", factREC(n2))
"""
working:
5 * facREC(4)
5 * 4 * facREC(3)
5 * 4 * 3 * fac(2)
5 * 4 * 3 * 2 * facREC(1)
5 * 4 * 3 * 2 * 1
"""

# Ques: REC for no in fibonacci series
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
       return fibo(n-1) +fibo(n-2)
print(fibo(3))
