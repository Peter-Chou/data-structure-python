from datastruct.algorithm import merge_sort, partition, quick_sort

import random


def test_merge_sort():
    seq = list(range(10))
    random.shuffle(seq)
    assert merge_sort(seq) == sorted(seq)


def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0


def test_quick_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    quick_sort(seq, 0, len(seq))
    assert seq == sorted_seq
