#!/usr/bin/python3
# Graham S. Paul (6-peak.py)
'''
Restores the peak of an disarranged list
'''
ret = int or None


def find_peak(list_of_integers) -> ret:
    '''
    Searches a number which is greater than both left
    and right
    '''

    listLen = len(list_of_integers)
    if listLen == 0:
        return None

    tmp = list_of_integers
    i = 0
    n = listLen - 1

    if tmp[i] > tmp[i+1]:
        return tmp[i]
    if tmp[n] > tmp[n-1]:
        return tmp[n]

    x = (i + n) // 2
    if tmp[x-1] < tmp[x] and tmp[x+1] < tmp[x]:
        return tmp[x]
    if tmp[x] < tmp[x-1]:
        return find_peak(tmp[i:x+1])
    if tmp[x] < tmp[x+1]:
        return find_peak(tmp[x:n+1])
    return tmp[i]
