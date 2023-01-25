print("TUTORIAL 22\n\n")

# 22.1 Python modules (Built-In)

''' (InBuilt modules) '''

# 1. RANDOM module
import random

rand = random.randint(0,100)
print(rand)

rand2 = random.random() * 1 # random no. b/w 0-1
                # can be altered by '*'
print(rand2)

lis = ["Star","DDZ","Sony","Viacom","ETV","+local"]
choice = random.choice(lis)


# 2. TIME module 
import time
t = time.time()
i = 0
while (i<100):
    print(i, end=" ")
    i +=1
t1 = time.time() - t
print("\n",t1, "sec")

ini = time.time()
for i in range(100):
    time.sleep(.5) # returns with a delay of 'n' secs
    print(i, end=" ")
t2 = time.time() - ini

print("\n",t2, "sec")

print(time.asctime(time.localtime(time.time())))

"""
.time() - returns no. of ticks
.localtime() - turns tick in local-time that too in form of tuple
.asctime() - returns the time tuple in presentable form
"""


# 3. OS module
import os
print(dir(os))

'''
os.cwd() # returns current working directory
os.chdir() # to change directory

os.listdir('directory loc.') # returns list of files in that directory
os.mkdir('name') # to make a new folder in that directory
         '/loc/name'
os.makedirs('outside/inside') # to make new folder inside a new folder
o.rename('old','new') # to change name of folder in directory

os.path.join('C://','/xyz') # joins path by excluding extra '/'s
os.path.exist('C://') # returns if path exits or not
os.path.isfile('C://') # returns if is file or not
    (isdir, isfile, isabs)

os.environ.get('Path') # returns environment variable's path
'''

# 4. Requests module


# 5. Json module


# 6. Pickle module


# 7. Regular Expression module
import re
'''

'''


# 22.2 Python modules (External)

'''
Readme: it contains general description or explained information about 
    the other files or software, it is advised to use it as a instruction set.
License: License and license file contain encrypted product passcodes for each 
    and every software that you have purchased.
'''
