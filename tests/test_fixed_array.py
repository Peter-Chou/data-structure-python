# -*- coding: utf-8 -*-

from datastruct.array import FixedArray


def test_array():
    size = 10
    a = FixedArray(size)
    a[0] = 1
    assert a[0] == 1

    a.clear()
    assert a[0] is None
