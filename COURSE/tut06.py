print("TUTORIAL 6 \n\n")

# 6.1 SET

l = [1, 2, 3, 4, 5]
s = set(l)  # inserting list indirectly
s1 = set([2, 32, "wee"])  # inserting directly
print(type(s))
print(type(s1))

# 6.2 FUNCTIONS

se = set()
se.add(212)
se.add(3)
se.add(2)
ss = se.intersection([212, 2])
ss1 = se.union([4, 56, 212])
print(ss, ss1)

"""
other functions include
 (from SET THEORY)
- .isdisjoint(_)
- .difference(_)
 and
- .max()
- .min()
- .len()
"""
