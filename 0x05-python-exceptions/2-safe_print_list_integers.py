#!/usr/bin/python3
# Graham S. Paul (2-safe_print_list_integers.py)
def safe_print_list_integers(my_list=[], x=0):
    """Creat first Elements of lista that are integers"""
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            pass
    print()
    return num
