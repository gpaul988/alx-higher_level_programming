#!/usr/bin/python3
# Graham S. Paul (0-positive_or_negative.py)

import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
