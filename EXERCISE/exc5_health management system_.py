print("EXERCISE 5:\nHealth Manager")

# BEGIN:

# taking data of per1, per2, per3
import datetime
def gettime():
    return datetime.datetime.now()

per = input("Enter 1: person1\nEnter 2: person2\nEnter 3: person3\n")
dta = input("Enter 1: FOOD\nEnter 2: EXERCISE\n")
typ = input("Enter 1: Log Data\nEnter 2: Retrieve Data\n")

if typ == 1:
    if per == 1:
        if dta ==1:
            file = open("p1FOOD.txt", 'a')
            log = input("Log:")
            file.write(gettime(),'\n',log)
            file.close
        elif dta ==2:
            file = open("p1EXC.txt", 'a')
            print("Enter:\n")
            log = input()
            file.write(gettime(),'\n',log)
            file.close
    elif per == 2:
        if dta ==1:
           file = open("p2FOOD.txt", 'a')
           log = input("Log:")
           file.write(gettime(),'\n',log)
           file.close        
        elif dta ==2:
           file = open("p2EXC.txt", 'a')
           log = input("Log:")
           file.write(gettime(),'\n',log)
           file.close           
    elif per == 3:
        if dta ==1:
           file = open("p3FOOD.txt", 'a')
           log = input("Log:")
           file.write(gettime(),'\n',log)
           file.close           
        elif dta ==2:
           file = open("p3EXC.txt", 'a')
           log = input("Log:")
           file.write(gettime(),'\n',log)
           file.close       

if typ == 2:
    if per == 1:
        if dta ==1:
            file = open("p1FOOD.txt")
            c = file.read()
            print(c)
            file.close 
        elif dta ==2:
            file = open("p1EXC.txt")
            c = file.read()
            print(c)
    elif per == 2:
        if dta ==1:
           file = open("p2FOOD.txt")
           c = file.read()
           print(c)     
        elif dta ==2:
           file = open("p2EXC.txt")
           c = file.read()
           print(c)    
    elif per == 3:
        if dta ==1:
           file = open("p3FOOD.txt")   
           c = file.read()
           print(c)     
        elif dta ==2:
           file = open("p3EXC.txt")
           c = file.read()
           print(c)    
