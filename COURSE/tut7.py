print("TUTORIAL 7 \n\n")

# 7.1 IF ELSE statement & MULTI IF
v = int(input())
v2 = 23
print("if else:")
if v2 > v:
    print("LESSER")  # checks every 'IF' statement
            # even when found correct
if v2 > v:  # (in IF ELSE ladder)
    print("LESSER")
else:
    print("equal")

print("\n\n")
print("elif:")
if v2 > v:
    print("LESSER")
elif v2 > v:
    print("LESSER")  # checks only once (in ELIF ladder) when found correct
else:
    print("equal")


# 7.2 LIST statement
print("\n\n")


# QUES: registered or not?
l1 = ["bhooms", "ashu", "parru 2.0", "bannu", "parru"]
print("NAME:")
n = input()
if n in l1:
    print("YES")
else:
    print("NO")
    print("YOU unregistered DUMB FUCK!")
    print("List:", l1)

print("\n\n")

# QUES: driving eligible or not?
print("AGE:")
a = int(input())
if a<6 or a>80:
    print("Get outta HERE!!")
if a==18:
    print("Ehhn!")
elif a<18:
    print("Nahh!")
else:
    print("Yeesh!")

# 7.2 ShortHand If Else
a=1
b=2
if a<b: print("BIGG") #one way

print("BIGG") if a<b else print("NAHH") # other way
