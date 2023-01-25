print("TUTORIAL 16\n\n")

# 16.1 *args & **kwargs
"""
*args - for list, tuple (taken as tuple)
**kwars - for dict (taken as dictionary)
"""
def _print(a,b,c,d,e): # Basic func ie. can take limited no. of inputs
    print(a,b,c,d,e)

_print("ashu","bhooms","bannu","paaru","paaru2")

def _printargs(n, *args, **kwargs): # args then kwargs argument should always be at last
    print(type(args))
    for item in args:
        print(item)
    print(n)
    for i,i2 in kwargs.items():
        print(i,"=",i2)
par = ["ashu","bhooms","bannu","paaru","paaru2"]
k = {"ashu": 1,"bhooms": 3,"bannu": 4,"paaru": 2,"paaru2": 5}
_printargs(5, *par, **k)

# 16.2 JOIN function

l = ["Bhooms","Ashu","Paru2","Paru","Bannu"]

for i in l:  # CONVENTIONAL method
    print(f"{i} and",end=" ")
print("ALL")

print("\n\n")

a = " and ".join(l) # JOIN method
print(a,"ALL")
