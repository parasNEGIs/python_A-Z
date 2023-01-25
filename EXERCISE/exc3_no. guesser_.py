print("EXERCISE 3:\nNo. GUESSER")

# BEGIN:

n = 83
print('LETS PLAY A GAME:\n----Number Guessing----\nEnter your GUESS')
ng = 0
for i in range(9):
    if ng != n:
        print("Try:")
        ng = int(input())
        if ng < n:
            print("EEEsh!! it be LIL")
        elif ng > n:
            print("WOOhuh!! it be BIGUH")
        else:
            print("YEEEESH!!! you got it\n----YOU WON----")
        if i == 8:
            print("_____GAME OVER_____\n\n")
    if ng == n:
        print("No of GUESSES you took:", i+1,  )
        break

