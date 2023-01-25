print("EXERCISE 6:\n----STONE-PAPER-SCISSOR Game----")

# BEGIN:
import random

print("ENTER:\nA: Paper\nS: Stone\nD: Scissor\n(YOU HAVE 10 CHANCES)\n***************************\n")
i = 0
co = 0
hu = 0
# 1,A: PAPER; 2,S: STONE; 3,D: SCISSOR;
while i < 10:
    print("PLAY:", end="")
    c = input()
    c.upper()
    r = random.randint(1,3)
    if r == 1:
        if c == 'A':
            i -=1
            print("  vs A\n__TIE__(chance not counted)")
        elif c == 'S':
            print("  vs A\n__YOU LOSE__") 
            co +=1
        elif c == 'D':
            print("  vs A\n__YOU WON__") 
            hu +=1
    elif r == 2:
        if c == 'S':
            i -=1
            print("  vs S\n__TIE__(chance not counted)")
        elif c == 'A':
            print("  vs S\n__YOU LOSE__") 
            co +=1
        elif c == 'D':
            print("  vs S\n__YOU WON__") 
            hu +=1
    elif r == 3:
        if  c == 'D':
            print("  vs D\n__TIE__(chance not counted)")
            i -=1
        elif c == 'S':
            print("  vs D\n__YOU LOSE__") 
            co +=1
        elif c == 'A':
            print("  vs D\n__YOU WON__") 
            hu +=1
    else:
        print("WRONG CHOICE retry\n(chance not counted)")
        continue
    i +=1
if hu < co:
    print(f"\n--GAME ENDS--\nBot:{co} vs You:{hu}\nNOPE !!")
   
elif hu > co:
    print(f"\n--GAME ENDS--\nYou:{hu} vs Bot:{co}\nYEEESH !!")

