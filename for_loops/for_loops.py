#  for loops = execute a block of code, a fixed number of times.
#              You can iterate over a range, string, sequence, etc.

""" count from 1 to 20 [whatever end +1]
for x in range(1 , 21):
    print(x)
"""

""" count backwards with reversed function
for x in reversed(range(1, 21)):
    print(x)

print("Happy Gizif Day!!!!")
"""

""" can include a step. below count from 1 and add 2 every time
for x in range(0 , 21, 2):
    print(x)
"""

""" can do string as well
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)
"""

#   key word = continue - can be in while loops as well
# below count will skip 13
"""
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
"""

#   key word = break - basically a stopping point
# below count gets to 13, stop and exit so count will be only to 12
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
