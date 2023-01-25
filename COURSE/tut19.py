print("TUTORIAL 19\n\n")

# 19.1 MAP function

# CONVENTIONAL method
num = ['1','2','32','33']
for i in range(len(num)):
    num[i] = int(num[i])

num[2] = num[2]+4
print(num[2])

# MAP method
num = list(map(str, num))

# Other uses with (LAMBDA func)

n = [2,4,3,1,43,55]
sq = list(map(lambda x: x*x, n))
print(sq)


# Ques- print Sq and Cube of list using MAP

def squr(i):
    return i*i

def cube(i):
    return i*i*i

func = [squr,cube]
print('ENTER nos in list\n','Enter list:')
n = int(input())
l = []
for i in range(n):
    l[i] = int(input())
    val = list(map(lambda x:x(i),func))
    print(val)


# 19.2 FILTER function

li = [2,235,65,33,24]
def greater_5(n):
    return num<5

gr = list(filter(greater_5,li))
print(gr)


# 19.3 REDUCE function

from functools import reduce

no = [1,2,3,4,]

cross = reduce(lambda x,y:x*y,no)
by = reduce(lambda x,y:x/y,no)
plus = reduce(lambda x,y:x+y,no)
less = reduce(lambda x,y:x-y,no)

