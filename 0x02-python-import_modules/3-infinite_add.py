#!/usr/bin/python3
# Graham S. Paul (3-infinite_add.py)

"""Pull the total of all arguments"""

if __name__ == "__main__":
    import sys
    result = 0
    if (len(sys.argv) > 1):
        for i in range(1, len(sys.argv)):
            result += (int(sys.argv[i]))
    print("{:d}".format(result))
