print("TUTORIAL 21\n\n")

# 21.0 IMPORT function
"""
note: do not use a MODULE name as that of file 
  it causes confusion for interpreter and importing module 
  function, then is not possible from that module
"""
import sys
print(sys.path) # shows path of SYS function 
 
from pygame import camera


# 21.1 Importing from FILES

from tut21testfile import a,b # particular variable
    # causes ambiguity when more than 1 file imported
print(a,f'\n{b}')

import tut21testfile # whole file
print(tut21testfile.c,tut21testfile.d)

tut21testfile.sample() # importing FUNCTIONS from a file
