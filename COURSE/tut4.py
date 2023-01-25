print("TUTORIAL 4 \n\n")

# 4.1 LIST
"""
list are mutable"""

l = [1, 10.00, "5w"]  # mixed list with all DATAtypes
print(l)
print(l[2])  # extraction

# 4.2 FUNCTIONS
l1 = [1, 32, 43, 2, 54, 1, 1]

l1.sort()  # changes in original LIST
print(l1)

l1.reverse()  # changes in original LIST
print(l1)

n = l1.count(1)
print(n)

print(len(l1))
print(max(l1))

l1.append(19)
l1.insert(2, 5)
l1.remove(1)  # removes 1st OCCURENCE
print(l1)

# 4.3 SLICING
print("\n\n")

l3 = [1, "ew", "₹12", 2.34, 696969]

print(l3[:])  # slicing
print(l3[::-1])  # EXTENDED slicing
l3[2] = "wow"
# 4.3 TUPPLE
"""
tupple are immutable"""

t = (1,2,3) # changing values not allowed
t2 = (4,) # extra comma at the end for SINGLE VALUE TUPPLE



