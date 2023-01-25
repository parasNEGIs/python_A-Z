from xmlrpc.client import boolean


print("EXERCISE 4:\nPATTERN PRINTING")

# BEGIN:
"""
TRUE:n    FALSE:n
*...     ****...
**       ***
***      **
****     *
     
"""
print("Enter no. of ROWS:")
n = int(input())
print("1 0r 0:")
b = bool(int(input()))
if b == True:
    for i in range(0,n):
        for j in range(0,i+1):
            print('*', end=" ")
        print("\n")

elif b == False:
    for i in range(n):
        for j in range(n,i,-1):
            print("*", end=" ")
        print()

