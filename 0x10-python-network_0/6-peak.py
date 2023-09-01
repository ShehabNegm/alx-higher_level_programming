#!/usr/bin/python3
def find_peak(list_of_integers):
    """find a peak on unsorted list"""

    st = list_of_integers
    list_length = len(st)
    if list_length == 0:
        return None
    lo = 0
    hi = list_length
    mid = lo + ((hi - lo) // 2)
    if hi == 1:
        return st[0]
    elif hi == 2:
        return max(st)
    else:
        if st[mid] >= st[mid - 1] and st[mid] >= st[mid + 1]:
            return st[mid]
        elif st[mid] < st[mid - 1] and mid > 0:
            return find_peak(st[:mid])
        elif st[mid] < st[mid + 1] and mid > 0:
            return find_peak(st[mid:])
