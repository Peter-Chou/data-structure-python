# -*- coding: utf-8 -*-


def bubble_sort(seq):
    """每次将最大的数字放到最右边
    """
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


def select_sort(seq):
    """每次将最小的数字放到最左边
    """
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]


def insert_sort(seq):
    """每次抽取一个数，按顺序正确放进已抽取的序列内
    """
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]   # 如果前面元素比pos大，则让前面元素往后移
            pos -= 1
        seq[pos] = value
