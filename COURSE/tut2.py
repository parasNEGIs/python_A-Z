print("TUTORIAL 2 \n\n")

# 2.1 VARIABLES

var1 = "hello"  # String
print("var1:", type(var1))
var2 = 4       # Integer
print("var2:", type(var2))
var3 = 32.33   # Floating point
print("var3:", type(var3))

concat = var1 + '!'
sum = var2 + var3
print(concat, sum)

# 2.2 TYPECASTING and other functions
v = 13.32
int(v)
str(v)
float(v)
"""
int-float,string
float-int,string
string-int (if digits), float (if digits)
"""
var1 = var1 + "\n"  # adding new line for better result
print(10 * var1)  # in STRING
v1 = var2 + var3
print(10 * v1)  # in digits works arithematically
print(10 * (str(v1) + "\n"))  # to use like string
# note use of commas

# 2.3 INPUTTING
"""note
default type of input variable is STRING"""
print("enter:")
i = input()
ino = int(input())
ino = str(ino * 1)
print("you entered:" + i + ino)

# 2.4 SWAPPING

a = 21
b = "coco"
a, b = b, a # swapping technique
print(a, b)
