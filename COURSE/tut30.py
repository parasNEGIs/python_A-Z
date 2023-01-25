print("TUTORIAL 30\n\n")

# 30.0 COROUTINES

def searcher():
    import time
    b = "Lorem ipsum dolor sit amet consectetur adipisicing elit. A, ducimus assumenda nemo minus doloribus, ratione itaque ex, officiis enim earum sint totam tempore voluptatem facere. Nihil asperiores eaque laudantium aut!"
    time.sleep(4)

    while True:
        t = (yield)
        if t in b:
            print(t,':present')
        else:
            print(t,'isn\'t present')

s = searcher()
print('SEARCHING...!!')
next(s)
print('NOW showing:')
input('press ENTER')
s.send('Lorem')
input('press ENTER')
s.send('isna')

s.close()

#input('press ENTER')
#s.send('isna') # will five STOP ITERATION error