#+-------------------------+
#| lab7b.py - Isaiah Grace |
#+-------------------------+

# Task 2 - For-loops and More Lists

mylist = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

# A --- print list as 3x3 block
for row in mylist:
    print(*row, sep='')

# B --- make all list elements *= 2 using nested for loops
for row in range(0, len(mylist)):
    mylist[row][:] = [num*2 for num in mylist[row]]

# C --- Extra
bigarray = []

for i in range(0, 10):
    bigarray += []
    for j in range(0, 10):
        bigarray[i] += '+' if i+j % 2
