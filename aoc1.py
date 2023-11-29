"""
One small step for man, one giant leap for Malina

"""

fuel = 0

file = open("input.txt", "r")

for line in file:
    mass = int(line)
    fuel += (mass//3 - 2)

print(fuel)

file.close()
