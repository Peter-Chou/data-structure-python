# -*- coding: utf-8 -*-

from ..queue.dll_quque import Deque


def test_dll_queue():
    size = 5
    dll = Deque(size)
    for i in range(size):
        dll.append(i)

    assert len(dll) == 5

    assert dll.pop() == 4
    assert dll.popleft() == 0
    assert dll.popleft() == 1

    # shoud be [2, 3]
    assert len(dll) == 2

    dll.append(5)
    dll.appendleft(-1)

    assert len(dll) == 4
    assert list(dll) == [-1, 2, 3, 5]
