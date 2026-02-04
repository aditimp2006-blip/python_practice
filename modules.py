# modules
# Using Python built-in modules

import math
import random

# Math module
print("Square root of 16:", math.sqrt(16))
print("Ceil of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))

# Random module
print("Random number 1-10:", random.randint(1, 10))
colors = ["red", "green", "blue"]
print("Random color:", random.choice(colors))
random.shuffle(colors)
print("Shuffled colors:", colors)
