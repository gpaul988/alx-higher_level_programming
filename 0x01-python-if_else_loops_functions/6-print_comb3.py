#!/usr/bin/python3
# Graham S. Paul (6-print_comb3.py)

"""Pull all attainable unlike union of two digits in increasing order.
    Both digits must be unlike - 01 and 10 are examined to be alike.
    """

for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print('{}{}'.format(digit1, digit2))
        else:
            print('{}{}'.format(digit1, digit2), end=',')
