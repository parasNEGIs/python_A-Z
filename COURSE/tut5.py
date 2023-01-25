print("TUTORIAL 5 \n\n")

# 5.1 DICTIONARY
"""
Dictionary is a set of key value pairs
(keys should be immutable)
"""
d1 = {}
print(type(d1))

d2 = {1: "one", 2: "two", 3: "three", 4: "four"} # dict
d2[5] = "five"  # insertion
print(d2)
print(d2[5])
del d2[5]
print(d2)
d2[5] = {} # creating nested key member
d2[5][5.1] = "five.one"
d2[5][5.2] = "five.two"
print(d2)

print("\n\n")

# 5.2 DICT function

d = d2        # here d acts as a new pointer to d2
        # which futher points to the dict, ie. changes in d2

d = d2.copy() # creates a copy indep. of d2
        # no changes in d2

print(d)

d.update({6:"six"}) # for insertion

print(d.get(6))     # extract particular key's value
print(d.items())    # all keys pairs
print(d.keys())     # only keys
print(d.values())   # only values
