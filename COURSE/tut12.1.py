# 12.1 Reading File functions
"""
"""
file = open("tut12.1.txt", "rt")  # first FILE name ,FILE mode(s)

cont = file.read()  # read first n characters
#print(file)
print("1")
for line in cont:  # extracts char by char (from the cont)
    print(line, end="")
print("\n\n2") # extracts line by line (from the file pointer)
# here doesnt print coz content has been extracted previously
for line in file:
    print(line)

file.close()
print("\n\n")
#other reading functions
file = open("tut12.1.txt")
print(file.readline()) # extracts first present line
print(file.readlines()) # extracts lines as tuple variables
