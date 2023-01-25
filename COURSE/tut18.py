print("TUTORIAL 18\n\n")

# 18.0 ENUMERATE functions
"""
  
"""

l = ['paru','bhooms','ashu','paru2','bannu']

i=1
for it in l:  #using conventional method
    if i%2 is not 0:
        print("buy:",it)
    i +=1

print('\n\n')

for ind,it in enumerate(l): #using ENUMERATE
    # here ind - index , it - item in that index
    if ind%2==0:
        print('buy:',it)