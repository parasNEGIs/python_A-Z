print("TUTORIAL 29\n\n")

# 29.0 FUNCTION caching

# Ex:
from functools import lru_cache
import time

'''
Cache- prestored data by system for  quick access of data
'''

@lru_cache
def work(n):
    time.sleep(n)
    return n

if __name__=='__main__':
 for i in range(6):    
    print("Running...")
    work(3)
    work(2)
    work(1)
    print('DONE!!!')

# 