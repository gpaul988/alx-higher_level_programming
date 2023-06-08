#!/usr/bin/python3
# Graham S. Paul (4-hidden_discovery.py)

"""Pull all name explained by hidden_4 model"""

if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if not i.startswith("__"):
            print("{:s}".format(i))
