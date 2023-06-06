#!/usr/bin/python3
# Graham S. Paul (3-print_alphabt.py)

for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
