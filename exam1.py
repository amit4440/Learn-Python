import numpy
import random

print("Random integers between 0 and 9: ")
for i in range(4, 15):
     y = random.randrange(9)
     print(y)

x = y.sort()

print("sorted array:")
print(x)
