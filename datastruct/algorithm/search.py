# -*- coding: utf-8 -*-


def binary_search(sorted_array, value):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1

    while beg <= end:
        mid = int((beg + end) / 2)
        if sorted_array[mid] == value:
            return mid
        elif sorted_array[mid] > value:
            end = mid - 1
        else:
            beg = mid + 1
    return -1
