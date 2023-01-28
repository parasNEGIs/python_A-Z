print("TUTORIAL 3 \n\n")

# 3.1 STRING functions
"""
String has indexes from 0-n
"""
st = "I am CODING !"

l= len(st) # length func.

# 3.2 SLICING (Substring func.)

print(st[0:3]) # inlcudes min excludes max
print(st[0:100]+"\n") # gets till end , no ERROR
print(st[::]) #EXTENDED SLICE takes default as 0 min and l max
              # takes 3rd as default 1 (skip none)
print(st[0:l:2]) # skips & gets every 2nd

print(st[-4:-2]) # negative INDICES
print(st[::-1]) # REVERSE
print(st[0]+"\n\n") # charAt func.
# print(st[100]) gets error

# 3.3 OTHER FUNCTIONS
# (no change in original form of STRING)
s = " I am COOL "

# BOOLEAN
print(s.isalnum()) # coz of spaces
print(s.isalpha()) # coz of spaces
print(s.isupper()) #checking if the string is in uppercase or not 
print(s.islower()) #checking if the string is in lowercase or not 
print(s.endswith("L "))

# INT
print(s.count(" "))
print(s.find("a")) # 1st occurrence

# STRING
print(s.capitalize())
print(s.swapcase())
print(s.lower())
print(s.upper())
print(s.replace(" ", "_"))
