from re import X
from typing import Dict


print("EXERCISE 1:\nDictionary")

# BEGIN:

Dic = {}
print('ENTER 5 words with meanings:')
for i in range(5):
      wd = input()
      Dic[wd] = input()

print(Dic)
print("\n\n__Get particular value__\nEnter word:")
In = input()
x = Dic.keys()
# list(x): not important though
print(type(x))
if In in (x):
      print(Dic.get(In))
else:
      print("GET OUT!! mul")

""" new method of INPUT 
i = input("ENTER:")
print(i)
"""