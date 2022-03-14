#+-------------------------+
#| lab7a.py - Isaiah Grace |
#+-------------------------+

# Task 1 - For-loops and Lists

import random

mylist = [8, 12, 90, -4, 6, 55, -1, 43, 108, 61]

# A ---
for num in mylist:
    print(num)

# B ---
mylist_mod = [num % 10 for num in mylist]

# C ---
for i in range(0, len(mylist)-1):
    mylist[i] = 0 if mylist[i] < 0 else mylist[i]

# D ---
odd_list = []
even_list = []

for i in range(1, 20, 2):
    odd_list.append(i)

for j in range(2, 21, 2):
    even_list.append(j)

full_list = []

for num in range(len(odd_list)):
    full_list.append(odd_list[num])
    full_list.append(even_list[num])

# E ---
nums = []
for i in range(1000):
    nums.append(random.randint(1,50))

for j in range(0, len(nums) - 4):
    if sum(nums[j:j+5]) == 50:
        print(f"Sum of nums[{j}]..nums[{j+5}] == 50. --> ", end='')
        print(f"{nums[j]}+{nums[j+1]}+{nums[j+2]}+{nums[j+3]}+{nums[j+4]}")

