print("TUTORIAL 25\nOOPs Concept\n--Theory session--")

# 25.01 OOPs Basics

""" Concept of D.R.Y.- Do not Repeat Yourself
Classes- ie. a TEMPLATE, helps in reusability
    of code 
Object- ie. INSTANCE of a class 

(for more insights regarding OOPs concept in general
 consult the 9-10th Curriculum Books)
""" 
# 25.02 ACCESS SPECIFIER

"""   Scope:
Public- everywhere 
Protected- inside the class and derived classes
Private- only inside class
"""
class Proc:
    p = 100     # public
    _p = 100    # protected
    __p  = 100  # private

em = Proc()
print(em._Proc__p) # deMangling
print(em._p)
print(em.p)