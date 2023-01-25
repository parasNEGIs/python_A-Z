# Seek() & Tell() functions
f = open("tut12.3.txt")

print(f.tell()) # to get the POSITION of pointer at that moment
print(f.readline()) # 1st line
print(f.tell())
print(f.readline()) # 2nd line
print(f.tell())

f.seek(0) # pointer returns to given position
print(f.readline())

f.close()

# Accessing FILE through BLOCK

with open("tut12.3.txt") as f: # Works as Opener and Closer of FILE
    a = f.read(4)
    print(a)