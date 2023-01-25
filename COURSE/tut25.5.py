# 25.51 ENCPSULATION
"""
#SETTER, GETTER, DELETER and Property Decorater
"""

class Empl:
    def __init__(self, fn, ln):
        self.fname = fn
        self.lname = ln
        #self.email = f"{self.fname}{self.lname}@NSK.com"
        # causes problem being in CONS.
    def explain(self):
        return f"This employee's:\nFirst name: {self.fname}\nLast Name: {self.lname}"
    @property # property decorator (GETTER)
    def email(self):
        if self.fname== None or self.lname== None:
            return "Email not set!!"
        return f"{self.fname}_{self.lname}@NSK.com"
    @email.setter
    def email(self, stri):
        n = stri.split('@')[0]
        self.fname = n.split('_')[0]
        self.lname = n.split('_')[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

an = Empl("Arsh", "UMRAO")
#print(an.explain()) 
# when through CONS no change was possible
print(an.email)

# here, to change name via email
an.email = "Varsh_UMRAO@NSK.com"
print("changed name:",an.fname)

# deletion

del an.email
print(an.email) 
# default new one none_none but now condition put


# 25.52 OBJECT introspection

# some functions for it:
sn = Empl("SS", "NN")

print(type(sn)) 
print(id(sn))
print(dir(sn))

import inspect
print(inspect.getmembers(sn))
# to get ATTRIBUTE, FUNCTIONS, VARIABLES of object
