from logging import exception


print("TUTORIAL 11\n\n")

# 11.1 TRY EXCEPT exception error handling

print("Enter 2 nos:")
num1= input()
num2= input()
try:
    print("Sum:", int(num1)+int(num2))
except Exception as exe:
    print(exe,'\n\n')

print("ab bhi ho gya!!!")

"""
note:
used usually when in INTERNET connectivity
"""
print('\n\n')

# 11.2 Else & Finally in Try Except

f1 = open('D:\PYTHON\py_COURSE\COURSE\\tut11.txt')

try:
    f = open('D:\PYTHON\py_COURSE\COURSE\\tut11.txt')
except Exception as e: # only when error exists (multiple EXCEPTs can be used for different errors)
    print(e)
else:  # runs only when no error exists ie. EXCEPT doesn't work
    print('ONLY RUNS if EXCEPT doesn\'t')

finally: # this block always works
    print('IMPORTANT!')
    f1.close()

print("STILL DONE\n\n")

''' Types of errors:
IO - input output error
EOF- end of file error

'''

# 'raise' keyword in Try Except

a = input("ENTER name?") 
if a.isnumeric():
    raise Exception("--SYNTAX ERROR--") #  futher code isn't executed

a = input("enter 2 no:")
b = input()
if a==0:
    raise ZeroDivisionError("NOOOPE!")

print('YEESH!')

# even more exceptions exist...