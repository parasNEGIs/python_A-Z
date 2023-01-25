# DIAMOND shape Problem
"""
Problem in MULTIPLE INHERITANCE
"""

class A:
    def met(self):
        print("CLASS A")

class B(A):
    # def met(self):
    #     print("CLASS B")
    pass

class C(A):
    def met(self):
         print("CLASS C")
    pass

class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()

d.met()
"""
SO here:
(in PYTHON)

D--->B , C
     |   |
    \/   \/
       A

precidence (at D):
 D > B > C > A
"""
