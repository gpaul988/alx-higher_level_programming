#!/usr/bin/python3
# Graham S. Paul (9-multiply_by_2.py)
def multiply_by_2(a_dictionary):
    new_dic = {}
    for key, value in a_dictionary.items():
        new_dic[key] = value * 2
    return new_dic
