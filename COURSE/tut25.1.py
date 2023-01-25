class SCH:
    House_kul= "UMRAO Negi"
    pass
    def details(self):
        return f"NAME-{self.name} and House-{self.House_kul}"    
s = SCH()
s.name = "---name---"
print(s.details(),"\n\n")


# 25.11 Classes in PYTHON

s1 = SCH()
s1.name = "PARIKSHIT"
s1.Sibl = ["PARAS","SAMARTH","BHOOMI","ASHISH"]

s2 = SCH()
s2.name = "PARAS"
s2.Sibl = ["PARIKSHIT","SAMARTH","BHOOMI","ASHISH"]

print(s1,s2,"\n\n") # Stored in different memory locations


# 25.12 Class & Instance VARIABLE

s3 = SCH()

print(SCH.House_kul,s1.House_kul,s2.House_kul) # House_kul being a CLASS variable
print(s1.Sibl,s2.Sibl) # Each Sibl being INSTANCE variable

s3.name = "noin"
s3.PERS = "whaa??"
s3.House_kul = "__none__" # INSTANCE variable for s3 is created of name HOUSE_kul

print(s3.__dict__) # Lists the VARIABLES 


# 25.13 CONSTRUCTOR 

class No2:
    Comp = "NEX.plc"
    def __init__(self, nm,  sal, ro):   # Constructor function __innit__ 
        self.name = nm
        self.salary = sal
        self.role = ro

#  25.14 CLASS methods and as a ALTERNATIVE constructor
    
    @classmethod # Class Method
    def change(cls, newcomp):
       cls.Comp = newcomp
    
    @classmethod # as constructor
    def fromSLASH(cls, string):
        prm = string.split("-")
        return cls(prm[0], prm[1], prm[2])
    """ (*args way) 
    def fromSLASH(cls, string):
        return cls(*string.split("-"))
    """
# 25.15 STATIC methods
    @staticmethod
    def printinguh(no):
        return (no*"Yeeshh!")

# Application in examples

n1 = No2("n1", 120000, "Consultant") # using CONSTRUCTOR 

n1.change("SOFTICS.grp") # using class method
print(n1.Comp)
print(No2.Comp)

n2 = No2.fromSLASH ("n1-200000-SeniorTECHY") # Constructor CLASS METHOD
print(n2.salary)

print(n2.printinguh(1)) # using STATIC method
"""
Static method:- is used when INSTANCES' VARIABLEs are not required to be produced to increase efficiency and for precise use of resources """


