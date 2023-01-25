# OVERLOADING & DUNDER methods

class COMP:
    Comp = "NEX.plc"
    def __init__(self, nm,  sal, ro): 
        self.name = nm
        self.salary = sal
        self.role = ro  
    
    def printdetails(self):
        return f"Name:{self.name}\nSalary:{self.salary}\nRole:{self.role}"
    
    @classmethod
    def change(cls, newcomp):
       cls.Comp = newcomp
    
    # DUNDER method (operator overloading)
    def __add__(self, other): # 1
        return self.salary+ other.salary
    
    def __repr__(self): # 2
        return f"COMP(\"{self.name}\", {self.salary}, \"{self.role}\")"
    
    def __str__(self): # 3
        return self.printdetails()
emp1 = COMP("1", 100000, "Techie")
emp2 = COMP("2", 10000, "HELPER")
print(emp1 + emp2) # implemented by DUNDER method
print(emp1) # (str > repr)
print(repr(emp1)) # would have print for str if repr were not present
