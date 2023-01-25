print("TUTORIAL 17\n\n")

# 17.1 String formatting

m = "I"
mm = "am"
m1 = "%s %s PARAS"%(m, mm) # String formatting
print(m1)

a= "{} {} PARAS"
b = a.format(m, mm) # FORMAT function
print(b)

# 17.2 F-strings (f=fast)

i = "have"
i2 = "YOU"
pr = f"GONNA {i} {i2}!! {3*23} times" # F string method
print(pr)
import math
print(f"N take that {math.cos(0)} thing.")
