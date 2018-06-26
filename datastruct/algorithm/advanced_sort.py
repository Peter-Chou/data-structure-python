# -*- coding: utf-8 -*-


def merge_sort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq)/2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
    # 合并两个有序的数组
    new_seq = merge_sorted_list(left_half, right_half)
    return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    """合并两个有序数组，返回一个新的有序数组"""
    len_a, len_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()

    while a < len_a and b < len_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    while a < len_a:
        new_sorted_seq.append(sorted_a[a])
        a += 1
    while b < len_b:
        new_sorted_seq.append(sorted_b[b])
        b += 1

    return new_sorted_seq


def quick_sort(arr, beg, end):
    """快速排序
    """
    if beg < end:
        pivot = partition(arr, beg, end)
        quick_sort(arr, beg, pivot)
        quick_sort(arr, pivot+1, end)


def partition(arr, beg, end):
    """快速排序的partition
    """
    pivot_index = beg   # 主元选第一个
    pivot = arr[pivot_index]
    left = pivot_index + 1
    right = end - 1     # 左闭右开  [0: end)

    while True:
        # left指针找比pivot大的
        while left <= right and arr[left] < pivot:
            left += 1
        # right指针找比pivot小的
        while right >= left and arr[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    return right    # 新的pivot位置
