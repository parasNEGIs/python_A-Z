# 12.21 Write-mode File functions
"""
"""
file = open("tut12.2.1.txt", "w") # here its WRITING mode

file.write("1. The first line")
# here content is embedded only once

file.close()

# 12.22 Append-mode File functions
"""
"""
file2 = open("tut12.2.2.txt", "a") # here its APPEND mode

file2.write("Yeesh!\n")
# here content 'same' content will be appended n times

a = file2.write("Yeesh!\n")
print(a)

file2.close()

"""
WRITE mode- jo bhi FILE me hai usse saaf kar do, aur jo
    ab likha jaa rha hai usse rkho.
APPEND mode- jo FILE me hai usse to rkho hi, aur saath 
    me isse jorh do.
"""

# 12.23 Read+Write mode
"""
"""
file3 = open("tut12.2.3.txt", "r+")

print(1, file3.read()) # here file contains -nil-, yet reads all
file3.write("additional content")
print(2, file3.read()) # here file contains a line, can't read even that as read func already invoked
