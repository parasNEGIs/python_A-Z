# 25.31 POLYMORPHISM

"""
(for more insights regarding OOPs concept in general
 consult the 9-10th Curriculum Books)
"""
# OVERRIDING

"""
precidence: of func or var
(instance var of self > instance var of parent >)self > parent > grand parent
one inherits var and func of parent and grandparent
"""

class A:
    cvar = "I am a HUNTER!!"
    def __init__(self):
        self.var1 = "She want to see my GUUN."
    
class B(A):
    var1 = "abcdefghijklmn"
    def __init__(self):
        super().__init__() # to access PARENT constructor
        self.var1 = "Yeesh!"
        
a = A()
b = B()

print(b.var1)
print(b.cvar)
