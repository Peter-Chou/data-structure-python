import random

import pytest

from datastruct.algorithm import bubble_sort, select_sort, insert_sort


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    bubble_sort(seq)
    assert seq == sorted_seq


def test_insert_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    insert_sort(seq)
    assert seq == sorted_seq


def test_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    select_sort(seq)
    assert seq == sorted_seq
