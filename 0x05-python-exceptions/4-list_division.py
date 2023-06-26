#!/usr/bin/python3
# Graham S. Paul (4-list_division.py)
def list_division(my_list_1, my_list_2, list_length):
    """Creates double list element"""
    newList = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            newList.append(div)
    return newList
