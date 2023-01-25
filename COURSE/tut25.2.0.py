# 25.21 ABSTRACTION & ENCAPSULATION

"""
(for more insights regarding OOPs concept in general
 consult the 9-10th Curriculum Books)
"""

# 25.22  INHERITANCE

class No2:
    Comp = "NEX.plc"
    def __init__(self, nm,  sal, ro): 
        self.name = nm
        self.salary = sal
        self.role = ro  
    @classmethod
    def change(cls, newcomp):
       cls.Comp = newcomp
    
    @classmethod
    def fromSLASH(cls, string):
        prm = string.split("-")
        return cls(prm[0], prm[1], prm[2])
    """ (*args way) 
    def fromSLASH(cls, string):
        return cls(*string.split("-"))
    """
    @staticmethod
    def printinguh(no):
        return (no*"Yeeshh!")