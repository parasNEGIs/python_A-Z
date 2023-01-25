# TYPES of INHERITANCE

class No2:
    Comp = "NEX.plc"
    def __init__(self, nm,  sal, ro):   # Constructor function __innit__ 
        self.name = nm
        self.salary = sal
        self.role = ro

# SINGLE inheritance

class Singl(No2): #Singl <- No2
    i = 5
    def __init__(self, nm, sal, ro, ln):
        self.languages = ln
        # super().__init__(nm, sal, ro) or also:
        self.name = nm
        self.salary = sal
        self.role = ro
    def prinp(self):
        return f"NAME: {self.name}\nSALARY: {self.salary}\nROLE:{self.role}\nLANG:{self.languages}"

ob1 = Singl("ob", 89000, "Junior engineer",['python','java', 'webD'])
ob2 = Singl('ob2', 100000, "engineer",['python','java', 'javascript', 'webD','OS&LIN+net'])
print(ob1.prinp())  # from No3 ie. child class
print(ob1.printinguh(3)) # from No2 ie. parent class

# MULTIPLE inheritance

class Multi:
    i = 10
    noOFgames = 4
    def __init__(self, name, gm):
        self.name = name
        self.noOFgames = gm
    def prin(self):
        return f"NAME:{self.name}\nGAMES:{self.noOFgames} "

class GUY(Singl, Multi):
# Checks CONST. in first CLASS ie. single. And will override with Var and Func of First CLASS
# Precidence: Self>1st Class>2nd Class
    pass

a = GUY("seksiBANNA",98000,'model',['sanskrit','hindi','tamil'])
print(a.i) # prints form only 1st class ie. Singl

# MULTILEVEL inheritance
"""
precidence: of func or var
(instance var of self > instance var of parent >)self > parent > grand parent
one inherits var and func of parent and grandparent
"""
class Dad:
    a1 = 1
    def a1(self):
        print(self.a1)

class Son(Dad):
    a2 = 1
    def a1(self):
        print(self.a2,"Weee!")

class GranSon(Dad):
    a3 = 1