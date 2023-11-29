"""
try it on number 100756 and 1969

"""

import math

sum = 0

file = open("input.txt", "r")
for line in file:
    line.strip()
    sum += (math.floor(int(line.strip())/3.) - 2)

print(sum)

file.close()
