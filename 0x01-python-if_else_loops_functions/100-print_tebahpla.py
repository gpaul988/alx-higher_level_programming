#!/usr/bin/python3
# Graham S. Paul (100-print_tebahpla.py)

for i in range(122, 96, -2):
    cs = f"{chr(i):s}{chr(i + ord('A') - ord('a') - 1):s}"
    print("{:s}".format(cs), end="")
