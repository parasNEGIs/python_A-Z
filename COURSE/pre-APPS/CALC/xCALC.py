# Version 2.0
print("\n\n_____BASIC arithmatic CALCULATOR____\n(Version 2.0)\n")
print('''\n___________COMMANDS__________
PRESS X : exit (after equation) PRESS X and X : exit (without equation)
PRESS enter: after equation , wrong input blank 
also:
x:- multiplication    /:-division
+:-addition           -:-subtraction
         ^:-exponential

Enter equation:''')

while True:
  eq = input()
  try:
    el = eq.split('+')
    print(float(el[0])+float(el[1]))
  except:
    pass
  try:
    el = eq.split('x')
    print(float(el[0])*float(el[1]))
  except:
    pass
  try:
    el = eq.split('-')
    print(float(el[0])-float(el[1]))
  except:
    pass
  try:
    el = eq.split('^')
    print(float(el[0])**float(el[1]))
  except:
    pass
  try:
    el = eq.split('/')
    print(float(el[0])/float(el[1]))
  except:
    pass
  w1=input()
  if w1=='X' or w1=='x':
    break
  else:
    pass