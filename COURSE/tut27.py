print("TUTORIAL 27\n\n")

# 27.1 COMPREHENSION

#  list comprehension

ls = []
for i in range(100):  # General METHOD
    if i%3==0:
        ls.append(i)
print(ls)

# COMPREHENSION method 
 
# (LIST)
ls2 = [i for i in range(100) if i%3==0]
print(ls2)

# (DICT)
dt = {i: f"item{i}" for i in range(1,101) if i%100==0}
dt2 = {value: key for key,value in dt.items()} # REVERSING
print(dt, dt2)

# (SET)
s = { dress for dress in ['d1','d2','d2','d1','d3','d1','d3']}
print(type(s),'\n',s)

# (GENERATORS)
# g = (i for i in(100) if i%2) 
# print(type(g),g.__next__)
# for i in g: # instead of NEXT
#     print(i)


# QUES: ask input and make a comprehension

def casy(argument):
    match argument:
        case '1':
           li =  [i for i in range(1,101) if i%3==0] 
           return print(li)
           
        case '2':
           di = {i: f'item {i}' for i in range(1,100) if i%3==0} 
           return print(di)
           
        case '3':
           si = { i for i in (3,6,9,12,15,18,21,24,27,30,"etc")}
           return print(si)
           
        case default:
           print("WRONG CHOICE!!")
            

print(''' (for divisors of 3 from 1 to 100) 
enter 1: LIST
enter 2: DICT
enter 3: SET''')

n = input()
casy(n)
