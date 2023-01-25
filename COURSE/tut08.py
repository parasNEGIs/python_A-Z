from random import randrange


print("TUTORIAL 8\n\n")
# LOOPS

# 8.1  FOR LOOP
a: int = 0
t = ([1, "one"], [98, "ninty eight"], ["weee", "ragdu"])
l1 = list(t)  # LOOPING in list or tupple
for i in l1:
    print(i)

print("\n\nDICT:")

di = dict(l1)  # LOOPING in dictionary
for i, l in di.items():  # i=key l=value
    print(l, "and mallab:")  # .items required for dict to extrct
    a = a + 1  # particular item (key and value)
    print('(', i, ')', a)

print("\n\n")

# in range()
for i in range(0,15,1): # starting val, last val (exc), change
    print(i)
for i in range(15,0,-1):
    print(i)


# QUES: check for digit and less or greater than 6
print("ANS:")
l = []
print("enter SIZE:")
c=0
for i in range(6):
    d = input()
    l.append(d)
"""
l = [6.6, 4, 5.4, 6, 7, 5] 
6.6 !!!YEEESH!!!
4 NAAH!! smaller
5.4 NAAH!! smaller
6 AHHHM!! MKK
7 !!!YEEESH!!!
5 NAAH!! smaller
"""
for i in l:
    s = str(i)
    if not s.isdigit() or s.replace('.', '', 1).isdigit():
        print(s,"Bruh YOU DUMB!!")
    else:
        if float(s) < 6:
            print(s,"NAAH!! smaller")
        elif float(s) == 6:
            print(s, "AHHHM!! MKK")
        else:
            print(s, "!!!YEEESH!!!")

"""
FETCHED

TO CHECK FOR 'float'(since no func is defined)

# initializing string
test_string = "45.657"

# printing original string
print("The original string : " + str(test_string))

# using isdigit() + replace()
# Check for float string
res = test_string.replace('.', '', 1).isdigit()

# print result
print("Is string a possible float number ? : " + str(res))
"""

# 8.2 WHILE LOOP
p=1
while(p<10):
    print(p)
    p= p+0.1


# 8.3 BREAK and CONTINUE keywords
p=0
while(True):
    p=p+1
    if p%2 != 0 and p<10:
        print(p)
    if p>10:
        break
    if p%2==0:
        print(p,"\"Ye to mera wala NO. hai!!\"")
        continue

# 8.4 PASS keyword
"""
creates a placeholder for future use.

When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
"""
a = 33
b = 200

if b > a: # in CONDITIONS
  pass

for x in [0, 1, 2]: # in LOOPS
  pass