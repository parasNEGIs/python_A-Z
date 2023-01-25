print("TUTORIAL 28\n\n")

# 28.0 ELSE with FOR loop

k = [1,2,3,4,5,6,7,8,9,0]

for i in k:
    if i==9:
        break # works only in  break statement
    else:
        print(i)
else: # not executed (loop terminated before end )
    print("Executed properly...")


for i in k:
    if i==9:
        continue # doesn't work here 
    else:
        print(i)
else: # executed (loop wasn't terminated)
    print("Executed properly...")


